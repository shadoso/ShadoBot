class Excluded:
    daily = ["es_ES", "fr", "pt_BR"]
    help = ["es_ES", "fr", "pt_BR"]
    ship = ["es_ES", "fr"]
    social = ["es_ES", "fr"]
    tarot = ["es_ES", "fr", "pt_BR"]


exclude = Excluded()

if __name__ == "__main__":
    print(exclude.social)
