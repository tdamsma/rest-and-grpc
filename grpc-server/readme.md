Simple threaded gRPC server that serves a (hardcoded) set of data 


Generate python from .proto with:

```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./meterusage.proto
```