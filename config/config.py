# Third-party
from pydantic_settings import BaseSettings

# Local
from absolute_path import list_to_path


class Settings(BaseSettings):
    SHADOBOT_AI: str
    DOMAIN: str
    POSTGRES_HOSTNAME: str
    POSTGRES_DB: str
    POSTGRES_PASSWORD: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
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
