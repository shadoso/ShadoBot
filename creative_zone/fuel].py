import random


class Quantropium():
    def __init__(
            self, natural: float = 0.4979, rarity: float = 4.2766,
            extraction: float = 0.5894, production: float = 1.0835,
            store: float = 0.6225, tax: float = 0.1472
    ):
        self.__price = natural + rarity * natural
        self.__tax = tax
        self.__list = [extraction, production, store]

    def fuel(self):
        full = self.__price
        for item in self.__list:
            full = full + item * full
        return list(float(f"{units * full:.2f}") for units in range(2, 15, 2))

    def price_table(self, discount: float = 0.011467):
        for price in self.fuel():
            shop = price - price * discount
            full = shop + shop * self.__tax
            print(f"{discount * 100:.2f}%")
            print(f"{full:.2f}")
            print(f"{shop * self.__tax:.2f}\n")
            discount += discount - discount * 0.67
        return 0


for loop in range(1):
    mod = random.uniform(4.2766, 139.2460)
    quan = Quantropium()
    print(f"Mod: {mod:.2f}")
    print(quan.price_table())
    print()