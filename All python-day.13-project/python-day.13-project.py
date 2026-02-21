from art import logo, vs
from game_data import data
import random


def high_follower(follower1, follower2):
    if follower1 > follower2:
        return "A"
    else:
        return "B"


def game():
    print(logo)
    score = 0
    game_continue = True

    account_a = random.choice(data)

    while game_continue:

        account_b = random.choice(data)

        while account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {account_a['name']}, {account_a['description']}, {account_a['country']}")
        print(vs)
        print(f"Against B: {account_b['name']}, {account_b['description']}, {account_b['country']}")

        user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

        real_answer = high_follower(
            account_a['follower_count'],
            account_b['follower_count']
        )

        if user_choice == real_answer:
            score += 1
            print(f"You're right! Current score: {score}.")
            account_a = account_b   # Important logic
        else:
            game_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")


game()