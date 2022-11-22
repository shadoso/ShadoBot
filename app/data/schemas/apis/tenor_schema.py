from pydantic import BaseModel
from typing import List


class Url(BaseModel):
    url: str


class Link(BaseModel):
    mediumgif: Url


class Formats(BaseModel):
    media_formats: Link


class Gif(BaseModel):
    results: List[Formats]

    def get_url(self):
        url = []

        for gif in self.results:
            url.append(gif.media_formats.mediumgif.url)

        return url
