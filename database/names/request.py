import json
from config.config import settings
import aiohttp
import asyncio
from pathlib import Path
from datetime import date
from database.session import database_session
from database.models.names import Forenames, ForenamesDetails

names_list = ['Renu', 'Rosario', 'Roy', 'Rabia', 'Rosemary', 'Rustam', 'Renato', 'Razia', 'Rolando', 'Renate', 'Randy',
              'Rehana', 'Rukhsana', 'Rogelio', 'Ratna', 'Ramona', 'Renata', 'Ron', 'Raphael', 'Ratan', 'Rabi', 'Rima',
              'Rohit', 'Rachid', 'Reynaldo', 'Rupa', 'Rasha', 'Reshma', 'Rania', 'Rinku', 'Roberta', 'Ray', 'Romeo',
              'Ralph', 'Rudolf', 'Renuka', 'Roshan', 'Rui', 'Rasool', 'Rick', 'Rahmat', 'Rajakumar', 'Rahim',
              'Rosemarie', 'Rocio', 'Rahima', 'Rames', 'Ramlatun', 'Reiko', 'Robina']

gender_path = f"/home/shadoso/Downloads/DataBaseBackup/Requests/Forenames/Gender/{date.today()}"
region_path = f"/home/shadoso/Downloads/DataBaseBackup/Requests/Forenames/Region/{date.today()}"


async def forebears_forenames(session, url: str):
    async with session.get(url) as response:
        data = await response.read()
        return json.loads(data)


async def forebears_request_regions():
    regions = [
        f"https://ono.4b.rs/v1/jur?key={settings.FOREBEARS_API}&name={forename}&type=forename" for forename in
        names_list
    ]

    async_tasks = []
    async with aiohttp.ClientSession() as session:
        for each_url in regions:
            async_tasks.append(
                asyncio.ensure_future(
                    forebears_forenames(
                        session=session,
                        url=each_url
                    ))
            )
        done = await asyncio.gather(*async_tasks)

        Path(region_path).mkdir()
        for index, region in enumerate(done):
            with open(region_path + f"/{index}.json", "w") as file:
                json.dump(region, file, indent=2)


async def forebears_request_genders():
    genders = [
        f"https://ono.4b.rs/v1/gen?key={settings.FOREBEARS_API}&forename={forename}" for forename in names_list
    ]

    async_tasks = []
    async with aiohttp.ClientSession() as session:
        for each_url in genders:
            async_tasks.append(
                asyncio.ensure_future(
                    forebears_forenames(
                        session=session,
                        url=each_url
                    ))
            )
        done = await asyncio.gather(*async_tasks)

        Path(gender_path).mkdir()
        for index, gender in enumerate(done):
            with open(gender_path + f"/{index}.json", "w") as file:
                json.dump(gender, file, indent=2)


async def main():
    await forebears_request_regions()
    await forebears_request_genders()


if __name__ == "__main__":
    pass
