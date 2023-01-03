from pydantic import BaseModel


class Languages(BaseModel):
    pt_BR: str = "pt_BR"
    default: str = "default"


class Attribute:
    name = "name"
    required = "required"
    valid = "valid"
    upright = "upright"
    inverted = "inverted"


def validating(language: str):
    option = Languages()
    language = language.replace("-", "_")

    if not hasattr(option, language):
        return option.default

    else:
        return language


if __name__ == "__main__":
    lis = ["pt-BR", "batata", "default"]
    for loop in lis:
        testing = validating(language=loop)
        print(testing)
