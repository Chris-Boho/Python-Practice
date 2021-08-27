import random

player_hand = input("What hand do you want to play? (Rock, Paper, Scissors)")

valid_hands = ["Rock", "Paper", "Scissors"]

if player_hand in valid_hands:
    print("That's a valid hand to play!")
else:
    print("That's NOT a valid hand to play!")

cpu_hand = random.choice(valid_hands)

def compare_hands(hand_one, hand_two):
    print("Rock - Paper - Scissors - SHOOT!")
    if hand_one == hand_two:
        print("Both hands are the same, so it's a TIE!")
    elif hand_one == "Rock" and hand_two == "Paper":
        print("Paper beats Rock! YOU LOSE!")
    elif hand_one == "Rock" and hand_two == "Scissors":
        print("Rock beats Scissors! YOU WIN!")
    elif hand_one == "Paper" and hand_two == "Rock":
        print("Paper beats Rock! YOU WIN!")
    elif hand_one == "Paper" and hand_two == "Scissors":
        print("Scissors beats Paper! YOU LOSE!")
    elif hand_one == "Scissors" and hand_two == "Rock":
        print("Rock beats Scissors! YOU LOSE!")
    elif hand_one == "Scissors" and hand_two == "Paper":
        print("Scissors beats Papers! YOU WIN!")

compare_hands(player_hand, cpu_hand)
