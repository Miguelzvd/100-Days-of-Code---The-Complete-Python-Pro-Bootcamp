import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_choices = ["rock", "paper", "scissors"]

move_options = [rock, paper, scissors]

player_choice = int(input("Choose your move: 1 for Rock, 2 for Paper, or 3 for Scissors: ")) - 1

computer_choice = random.randint(0, 2)

print(f"Your move({game_choices[player_choice]}):\n" + move_options[player_choice])

print(f"Computers move({game_choices[computer_choice]}):\n" + move_options[computer_choice])

while 0 < player_choice > 2:
    player_choice = int(input("Please choose only 1 (Rock), 2 (Paper), or 3 (Scissors)."))

if player_choice == 0 and computer_choice == 2:
    print(f"You won! You chose: {game_choices[player_choice]}")

elif computer_choice == 0 and player_choice == 2:
    print(f"You lost! You chose: {game_choices[player_choice]}")

elif player_choice > computer_choice:
    print(f"You won! You chose: {game_choices[player_choice]}")

elif computer_choice > player_choice:
    print(f"You lost! You chose: {game_choices[player_choice]}")

elif player_choice == computer_choice:
    print(f"It's a tie! Both chose {game_choices[player_choice]}")

# OR

# elif game_choices[player_choice] == "paper" and game_choices[computer_choice] == "scissors":
#     print(f"You lost! You chose: {game_choices[player_choice]}")
#
#     print(f"Your move({game_choices[player_choice]}):\n" + move_options[player_choice])
#
#     print(f"Computers move({game_choices[computer_choice]}):\n" + move_options[computer_choice])
#
# elif game_choices[player_choice] == "scissors" and game_choices[computer_choice] == "paper":
#     print(f"You won! You chose: {game_choices[player_choice]}")
#
#     print(f"Your move({game_choices[player_choice]}):\n" + move_options[player_choice])
#
#     print(f"Computers move({game_choices[computer_choice]}):\n" + move_options[computer_choice])
#
# elif game_choices[player_choice] == "rock" and game_choices[computer_choice] == "paper":
#     print(f"You lost! You chose: {game_choices[player_choice]}")
#
#     print(f"Your move({game_choices[player_choice]}):\n" + move_options[player_choice])
#
#     print(f"Computers move({game_choices[computer_choice]}):\n" + move_options[computer_choice])
#
# elif game_choices[player_choice] == "paper" and game_choices[computer_choice] == "scissors":
#     print(f"You won! You chose: {game_choices[player_choice]}")
#
#     print(f"Your move({game_choices[player_choice]}):\n" + move_options[player_choice])
#
#     print(f"Computers move({game_choices[computer_choice]}):\n" + move_options[computer_choice])
#
# elif game_choices[player_choice] == "scissors" and game_choices[computer_choice] == "rock":
#     print(f"You lost! You chose: {game_choices[player_choice]}")
#
#     print(f"Your move({game_choices[player_choice]}):\n" + move_options[player_choice])
#
#     print(f"Computers move({game_choices[computer_choice]}):\n" + move_options[computer_choice])
#
# elif game_choices[player_choice] == "rock" and game_choices[computer_choice] == "scissors":
#     print(f"You won! You chose: {game_choices[player_choice]}")
#
#     print(f"Your move({game_choices[player_choice]}):\n" + move_options[player_choice])
#
#     print(f"Computers move({game_choices[computer_choice]}):\n" + move_options[computer_choice])