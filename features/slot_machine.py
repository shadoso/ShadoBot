from numpy.random import choice
from statistics import mode

KEY = 0
VALUE = 1
TWICE = 2
THRICE = 3
PROBABILITY = [0.30, 0.265, 0.179, 0.129, 0.073, 0.035, 0.019]
NOTHING = ":x:"
CHERRY = ":cherries:"
BLUEBERRY = ":blueberries:"
COIN = ":coin:"
CARD = ":credit_card:"
GEM = ":gem:"
EIGHTBALL = ":8ball:"

SLOT = [NOTHING, CHERRY, BLUEBERRY, COIN, CARD, GEM, EIGHTBALL]
JACKPOT = {NOTHING * THRICE: 0,
           CHERRY * THRICE: 50,
           CHERRY * TWICE: 0.5,
           BLUEBERRY * THRICE: 150,
           BLUEBERRY * TWICE: 0.7,
           COIN * THRICE: 500,
           COIN * TWICE: 1.5,
           CARD * THRICE: 1500,
           GEM * THRICE: 2500,
           EIGHTBALL * THRICE: 25000
           }

average = []


class SlotMachine:
    def __init__(self, cash):
        self.cash = cash

    @staticmethod
    def spin():
        row = choice(SLOT, size=THRICE, p=PROBABILITY)
        key = "".join(row[:])
        if key.count(CHERRY) == TWICE or key.count(BLUEBERRY) == TWICE or key.count(COIN) == TWICE:
            key = mode(row) * TWICE
        return key, "".join(row)

    def pot(self):
        result = self.spin()
        key = result[KEY]
        value = result[VALUE]
        if key in JACKPOT:
            cash = JACKPOT[key] * self.cash
            return cash, value
        else:
            return value
