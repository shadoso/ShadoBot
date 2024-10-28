from config.constants import DEFAULT_


async def verify_language(language: str, language_keys: dict):
    language = language.replace("-", "_")
    return language if language in language_keys.keys() else DEFAULT_
