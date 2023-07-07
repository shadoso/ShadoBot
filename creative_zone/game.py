from numpy.random import choice
from numpy import unique, multiply

player = {
    index: [[0] * 3 for _ in range(3)] for index in range(2)
}
dice = [d for d in range(1, 7)]
current = 1


def result(arr: list):
    listin = []
    for r in arr:
        un, coun = unique(r, return_counts=True)
        listin.append(sum(multiply(un, coun ** 2)))

    return listin, sum(listin)


def purge(grid: int, dice_result: int, rival: int):
    if dice_result in player[(rival + 1) % 2][grid]:
        player[(rival + 1) % 2][grid] = [0 if dice_result == num else num for num in player[(rival + 1) % 2][grid]]
    else:
        pass


def available(current: int, player: list) -> list:
    return [index + 1 for index, grid in enumerate(player[current]) if 0 in grid]


while True:
    current = (current + 1) % 2
    x = choice(dice)
    print("----------")
    availabl = available(current=current, player=player)
    position = int(input(f"Dado: {x}\nEscolha uma das colunas{availabl}: "))
    print("----------")
    player[current][position].pop(0)
    player[current][position].append(x)
    purge(grid=position, dice_result=x, rival=current)
    availabl = available(current=current, player=player)
    print(f"Player 1:{player[0]}\nScore:{result(player[0])}\n")
    print(f"Player 2:{player[1]}\nScore:{result(player[1])}")

    if not any(availabl):
        break

print(player)
