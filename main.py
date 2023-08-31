from pywhispercpp.model import Model
from fastapi import FastAPI
from starlette.responses import Response

from sonarr import Sonarr

app = FastAPI()
model = Model('medium', models_dir="models/", n_threads=4)


@app.post("/sonarr")
async def create_anime(sonarr: Sonarr):
    return Response(status_code=200)
