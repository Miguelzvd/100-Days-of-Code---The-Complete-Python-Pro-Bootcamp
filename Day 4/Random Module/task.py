import random

# rand_num = random.randint(1, 10)
# print(rand_num)

# random_num_0_to_1 = random.random() * 10
# print(random_num_0_to_1)

# random_float = random.uniform(1, 10)
# print(random_float)

coin_side = ""

side = random.randint(0, 1)

if side == 0:
    coin_side = "heads"

else:
    coin_side = "tails"

print(f"coin side is: {coin_side}")

# OR

# random_coin_side = random.randint(0, 1)
#
# if random_coin_side == 0:
#     print(f"coin side is: tails")
#
# else:
#     print(f"coin side is: heads")

