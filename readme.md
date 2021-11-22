# Demo app combining REST and gRPC

This demo serves a simple dataset with a rest endpoint via a gRPC service. The gRPC and REST servicies each run in a seperate docker container.

To run the demo:

```bash
git clone git@github.com:tdamsma/rest-and-grpc.git
cd rest-and-grpc
docker-compose up
```

And the visit http://localhost:5000/

## Development notes

Though not a strict requirement, this package is devloped with vscode devcontainers. The required config is included.

The app consists of a gRPC server and a RESTful server that also serves a static index.html file on the root. See below how to run the servers for development.
Both servers must be running for the demo to work
 
### REST server

Using FastAPI framework

Start with:

```bash
uvicorn rest-server.main:app --port=5000 --host=0.0.0.0 --reload
```

### gRPC server

Using the gRPC framework

Start with:

```bash
python grpc-server/server.py
```
There is also a test client included, which can be run with
```bash
python grpc-server/client.py
```
