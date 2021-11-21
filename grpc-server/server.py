"""gRPC server for meterusage data from a csv file."""

import logging
from concurrent import futures

import grpc
import meterusage_pb2
import meterusage_pb2_grpc
import pandas as pd
from google.protobuf.timestamp_pb2 import Timestamp

logger = logging.getLogger("grpc-server")


def datetime_to_timestamp(t: pd.Timestamp):
    # note that python time precision is only up to microseconds
    # the conversion will not be exact
    seconds = int(t.timestamp())
    nanos = int((t.timestamp() - seconds) * 1e9)
    return Timestamp(seconds=seconds, nanos=nanos)


class MeterUsageService(meterusage_pb2_grpc.GetMeterUsageServicer):
    def ReturnMeterUsage(self, request, context) -> meterusage_pb2.MeterUsageReply:
        logger.debug(request)
        df = pd.read_csv("data/meterusage.csv", parse_dates=["time"])

        return meterusage_pb2.MeterUsageReply(
            meterusage=(
                meterusage_pb2.MeterUsageReply.MeterUsageEntry(
                    time=datetime_to_timestamp(tup.time),
                    meterusage=tup.meterusage,
                )
                for tup in df.itertuples()
            )
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    meterusage_pb2_grpc.add_GetMeterUsageServicer_to_server(MeterUsageService(), server)
    server.add_insecure_port("0.0.0.0:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logger.debug("Starting gRPC server")
    serve()
