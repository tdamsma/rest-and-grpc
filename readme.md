# Demo app combining REST and gRPC

## Development notes
### REST server

Using FastAPI framework

Start with:

```bash
uvicorn rest-server.main:app --port=5000 --reload
```


### gRPC server

Using the gRPC framework

Start with:

```bash
python grpc-server/server.py
```