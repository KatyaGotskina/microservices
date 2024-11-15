from fastapi import FastAPI, Request, Response
from pydantic import BaseModel
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

from metrics_middleware import MetricsMiddleware

app = FastAPI()
app.add_middleware(MetricsMiddleware)


class DoRequest(BaseModel):
    message: str


@app.post("/")
async def do(body: DoRequest):
    return {"result": body.message[:5]}


@app.get("/metrics")
async def metrics():
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)
