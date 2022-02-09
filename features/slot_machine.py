from numpy.random import choice
from numpy import array_equal

SLOT = [":x:", ":cherries:", ":blueberries:", ":coin:", ":credit_card:", ":gem:", ":8ball:"]
TRIPLE = 3
DOUBLE = 2
JACKPOT = {":x:" * TRIPLE: 0,
           ":cherries:" * TRIPLE: 50,
           ":cherries:" * DOUBLE: 7,
           ":blueberries:" * TRIPLE: 150,
           ":blueberries:" * DOUBLE: 22,
           ":coin:" * TRIPLE: 500,
           ":coin:" * DOUBLE: 75,
           ":credit_card:" * TRIPLE: 1500,
           ":gem:" * TRIPLE: 2500,
           ":8ball:" * TRIPLE: 25000
           }

PROBABILITY = [0.30, 0.265, 0.179, 0.129, 0.073, 0.035, 0.019]
average = []


class SlotMachine:
    def __init__(self, cash):
        self.cash = cash

    @staticmethod
    def spin():
        row = choice(SLOT, size=TRIPLE, p=PROBABILITY)
        key = "".join(row)
        return key

    def pot(self):
        result = self.spin()
        print(result)
        if result in JACKPOT:
            return JACKPOT[result]

        else:
            return None


if __name__ == '__main__':
    jacks = SlotMachine(100)
    while len(average) < 2:
        guess = jacks.pot()
        if guess is not None:
            average.append(guess)

    print(average)
