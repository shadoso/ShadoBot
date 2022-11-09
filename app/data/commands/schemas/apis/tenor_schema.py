from pydantic import BaseModel
from typing import List


class Url(BaseModel):
    itemurl: str


class Gif(BaseModel):
    results: List[Url]

    def get_url(self):
        url = []

        for gif in self.results:
            url.append(gif.itemurl)

        return url
