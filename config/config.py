# Third-party
from pydantic_settings import BaseSettings

# Local
from absolute_path import list_to_path


class Settings(BaseSettings):
    DATABASE_HOSTNAME: str
    DATABASE_NAME: str
    DATABASE_PASSWORD: str
    DATABASE_PORT: int
    DATABASE_USERNAME: str
    DISCORD_ID: str
    DISCORD_KEY: str
    DISCORD_URL: str
    FOREBEARS_API: str
    HASH_ALGORITHM: str
    SECRET_KEY: str
    TELEGRAM_API: str
    TELEGRAM_CHAT_ID: int
    TENOR_API: str
    TENOR_CKEY: str

    class Config:
        env_file = list_to_path(file_path=["config", ".env"])


settings = Settings()

if __name__ == "__main__":
    print(settings.DISCORD_URL)
