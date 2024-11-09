name1 = "Abigail"
name2 = "Abigaille"


def normalizer(text: str):
    from unicodedata import normalize

    return normalize("NFKD", text).encode("ASCII", "ignore").decode("utf-8").lower()


def similarity(original: str, compare: str):
    from config.constants import PERCENTAGE_
    from Levenshtein import distance, ratio

    weights = (1, 1, 2)
    length = max(len(original), len(compare))

    resemblance = distance(
        normalizer(original),
        normalizer(compare),
        weights=weights
    )
    proportion = ratio(
        original,
        compare
    )
    return (proportion + (length - resemblance) / length) / 2 * PERCENTAGE_


print(similarity(original=name1, compare=name2))
