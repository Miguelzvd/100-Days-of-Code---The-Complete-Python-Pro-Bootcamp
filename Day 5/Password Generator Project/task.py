import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""

# Easy Version

# for letter in range(1, nr_letters + 1):
#     password += random.choice(letters)

# for symbol in range(1, nr_symbols + 1):
#     password += random.choice(symbols)

# for number in range(1, nr_numbers + 1):
#     password += random.choice(numbers)

# print(password)

# Hard Version

password_list = []

for letter in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for symbol in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

for number in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)


for char in password_list:
    password += char

print(password)

# OR

# total_of_characters = nr_letters + nr_symbols + nr_numbers
#
# for character in range(1, total_of_characters + 1):
#     random_character = random.randint(0, 2)
#
#     if random_character == 0:
#         password += random.choice(letters)
#     if random_character == 1:
#         password += random.choice(symbols)
#     if random_character == 2:
#         password += random.choice(numbers)
#
# print(password)


