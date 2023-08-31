from pydantic import BaseModel
from typing import List


class Episode(BaseModel):
    id: int
    episodeNumber: int
    seasonNumber: int
    title: str
    airDate: str
    airDateUtc: str


class EpisodeFile(BaseModel):
    id: int
    relativePath: str
    path: str
    quality: str
    qualityVersion: int
    releaseGroup: str
    size: int


class Series(BaseModel):
    id: int
    title: str
    path: str
    tvdbId: int
    tvMazeId: int
    imdbId: str
    type: str


class Sonarr(BaseModel):
    series: Series
    episodes: List[Episode]
    episodeFile: EpisodeFile
    isUpgrade: bool
    eventType: str
