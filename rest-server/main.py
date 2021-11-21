from typing import Optional
from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel, validator
import csv
import math


app = FastAPI()


class MeterUsageEntry(BaseModel):
    time: datetime
    meterusage: Optional[float] = None

    @validator("meterusage")
    def meterusage_isfinite(cls, v) -> Optional[float]:
        return v if math.isfinite(v) else None


class MeterUsage(BaseModel):
    meterusage: list[MeterUsageEntry]


@app.get("/meterusage")
def read_meterusage():
    with open("data/meterusage.csv") as f:
        meterusage = MeterUsage(
            meterusage=[
                MeterUsageEntry(**row)
                for row in csv.DictReader(f, skipinitialspace=True)
            ]
        )
    return meterusage


@app.get("/meterusage_entry")
def read_meterusage_entry():
    return MeterUsageEntry(time=datetime.now(), meterusage=1)
