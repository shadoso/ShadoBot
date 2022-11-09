from pydantic import BaseSettings
from abs_pth import arquive


class Settings(BaseSettings):
    DATABASE_HOSTNAME: str
    DATABASE_NAME: str
    DATABASE_PASSWORD: str
    DATABASE_PORT: str
    DATABASE_USERNAME: str
    DISCORD_ID: str
    DISCORD_KEY: str
    DISCORD_URL: str
    TENOR_API: str
    CKEY: str

    class Config:
        where = ["config", ".env"]
        env_file = arquive(where=where)


settings = Settings()

if __name__ == "__main__":
    print(settings.DISCORD_URL)
