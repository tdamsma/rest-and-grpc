import logging
import math
import os
import sys
import uuid
from datetime import datetime
from typing import Optional

import grpc
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, validator

sys.path
sys.path.append("grpc-server")

import meterusage_pb2
import meterusage_pb2_grpc

app = FastAPI()

grpc_host = os.getenv("GRPC_HOST", "localhost")
grpc_post = os.getenv("GRPC_PORT", "50051")


logger = logging.getLogger("rest-server")

log_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(levelprefix)s %(asctime)s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    },
    "loggers": {
        "rest-server": {"handlers": ["default"], "level": "DEBUG"},
    },
}
logging.config.dictConfig(log_config)


class MeterUsageEntry(BaseModel):
    time: datetime
    meterusage: Optional[float] = None

    @validator("meterusage")
    def meterusage_isfinite(cls, v) -> Optional[float]:
        return v if math.isfinite(v) else None

    @classmethod
    def from_grpc(
        cls, entry: meterusage_pb2.MeterUsageReply.MeterUsageEntry
    ) -> "MeterUsageEntry":
        return cls(
            time=datetime.fromtimestamp(
                entry.time.seconds + entry.time.nanos / 1_000_000_000
            ),
            meterusage=entry.meterusage,
        )


class MeterUsage(BaseModel):
    meterusage: list[MeterUsageEntry]


@app.get("/meterusage")
async def read_meterusage():
    async with grpc.aio.insecure_channel(f"{grpc_host}:{grpc_post}") as channel:
        stub = meterusage_pb2_grpc.GetMeterUsageStub(channel)
        identifier = str(uuid.uuid4())
        logger.debug(f"Sending request for meterusage with {identifier=}")
        response = await stub.ReturnMeterUsage(
            meterusage_pb2.MeterUsageRequest(identifier=identifier)
        )

    return [MeterUsageEntry.from_grpc(entry) for entry in response.meterusage]


app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
