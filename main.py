from pywhispercpp.model import Model
from fastapi import FastAPI
from sonarr import Sonarr

import pysubs2
from pysubs2 import SSAFile, SSAEvent

app = FastAPI()

@app.post("/sonarr")
async def create_anime(sonarr: Sonarr):
    return sonarr


model = Model('medium', models_dir="models/", n_threads=4)
segments = model.transcribe('Sla.m4a', speed_up=True)
subs = SSAFile()
for seg in segments:
    event = SSAEvent(start=seg.t0 * 10, end=seg.t1 * 10)
    event.plaintext = seg.text.strip()
    subs.append(event)
subs.save(path="test.srt")
