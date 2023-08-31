from pywhispercpp.utils import output_srt
from pywhispercpp.model import Model
import os


def change_extension(file_path, new_extension):
    base = os.path.splitext(file_path)[0]
    return f"{base}.{new_extension}"


def transcribe(model: Model, mediaFilePath: str):
    segments = model.transcribe(mediaFilePath, speed_up=True)
    output_srt(segments, output_file_path=change_extension(mediaFilePath, "srt"))
    return True
