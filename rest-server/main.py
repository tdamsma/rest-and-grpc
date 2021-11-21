import math
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
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        stub = meterusage_pb2_grpc.GetMeterUsageStub(channel)
        response = await stub.ReturnMeterUsage(
            meterusage_pb2.MeterUsageRequest(identifier=str(uuid.uuid4()))
        )

    return [MeterUsageEntry.from_grpc(entry) for entry in response.meterusage]


app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
