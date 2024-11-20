import art
import random


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def score_sum(cards):
    """Returns the sum of the cards from the deck"""
    if 11 in cards and 10 in cards and len(cards) == 2:
       return 0
    return sum(cards)


def who_won(user, computer):
    """Returns the winner"""
    if user > 21:
        print("You went over. You lose 😭")
        return
    elif computer > 21:
        print("Opponent went over. You win 😁")
    elif computer > user:
        print("You lose 😤")
        return
    elif user == 21 or user > computer:
        print("You win 😃")
        return
    print("Its a draw :)")
    return


will_play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

should_play = False

if will_play_again == "y":
    should_play = True

while should_play:

    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]

    # or

    # for _ in range(2):
    #     user_cards.append(deal_card())
    #     computer_cards.append(deal_card())

    user_score = score_sum(user_cards)
    computer_score = score_sum(computer_cards)

    print(art.logo)

    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    continue_drawing = True

    while user_score < 21 and continue_drawing:
        draw_new_card = input("Type 'y' to draw another card or 'n' to pass: ")

        if draw_new_card == "y":
            user_cards.append(deal_card())
            user_score = score_sum(user_cards)
            print(f"Your cards: {user_cards}, current score: {user_score}")
            print(f"Computer's first card: {computer_cards[0]}")

        else:
            continue_drawing = False

    while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = score_sum(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    who_won(user_score, computer_score)

    should_play = False

    will_play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")

    if will_play_again == "y":
        should_play = True
