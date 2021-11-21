"""Async client for the server for testing purposes."""

from __future__ import print_function

import asyncio
import logging
import uuid

import grpc
import meterusage_pb2
import meterusage_pb2_grpc


async def make_request():
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        stub = meterusage_pb2_grpc.GetMeterUsageStub(channel)
        response = await stub.ReturnMeterUsage(
            meterusage_pb2.MeterUsageRequest(identifier=str(uuid.uuid4()))
        )
        print(f"Greeter client received: {response=}")


async def run() -> None:
    await asyncio.gather(*(make_request() for i in range(5)))


if __name__ == "__main__":
    logging.basicConfig()
    asyncio.run(run())
