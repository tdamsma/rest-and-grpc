import logging
import time
from concurrent import futures

import grpc
from google.protobuf.timestamp_pb2 import Timestamp

import meterusage_pb2
import meterusage_pb2_grpc


class Greeter(meterusage_pb2_grpc.GetMeterUsageServicer):
    def ReturnMeterUsage(self, request, context):
        timestamp = Timestamp()
        timestamp.GetCurrentTime()
        print(f"received {request=}")
        time.sleep(2)
        print(f"done processing  {request=}")

        return meterusage_pb2.MeterUsageReply(
            meterusage=[
                meterusage_pb2.MeterUsageReply.MeterUsageEntry(
                    time=timestamp, meterusage=1.23
                ),
                meterusage_pb2.MeterUsageReply.MeterUsageEntry(
                    time=timestamp, meterusage=3.45
                ),
            ]
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    meterusage_pb2_grpc.add_GetMeterUsageServicer_to_server(Greeter(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
