# from app.data.schemas.game import coordinates_schemas as group
# import random
#
# nums = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
# all_names = []
# for loop in range(50):
#     universe = random.choice(list(group.Universes))
#     sector = random.choice(list(group.Sector))
#     names = random.sample(list(group.GalaxyNames), random.randint(1, 3))
#
#     full = universe.value, sector.value, ' '.join(nome.value for nome in names), random.choice(nums)
#     if full not in all_names:
#         all_names.append(" ".join(full))
#
# print(all_names)
#
#
# min = 0.02
# max = 1300
import random

for loop in range(26):
    ax_x = random.randint(-142563922011, 692563955030)
    ax_y = random.randint(-142563922011, 692563955030)
    print(f"X:{ax_x}, Y:{ax_y}")
    print()