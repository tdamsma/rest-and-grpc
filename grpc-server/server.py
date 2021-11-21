# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

import logging
from concurrent import futures
from datetime import datetime
import grpc
import meterusage_pb2
import meterusage_pb2_grpc


class MeterUsage(meterusage_pb2_grpc.GetMeterUsageServicer):
    def ReturnMeterUsage(self, request, context):
        return meterusage_pb2_grpc.MeterUsageReply(
            [meterusage_pb2_grpc.MeterUsageEntry(time=datetime.now(), meterusage=1)]
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    meterusage_pb2_grpc.add_GetMeterUsageServicer_to_server(MeterUsage(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
