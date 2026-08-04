import random

choices = {
    "1": "Rock",
    "2": "Paper",
    "3": "Scissors"
}


def determine_winner(player, computer):

    if player == computer:
        return "Draw"

    if (
        (player == "Rock" and computer == "Scissors") or
        (player == "Paper" and computer == "Rock") or
        (player == "Scissors" and computer == "Paper")
    ):
        return "Win"

    return "Lose"


def play_round():

    print("\nChoose your move")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    while True:
        choice = input("\nEnter your choice: ")

        if choice in choices:
            break

        print("Invalid choice. Try again.")

    player = choices[choice]
    computer = random.choice(list(choices.values()))

    print(f"\nYou: {player}")
    print(f"Computer: {computer}")

    result = determine_winner(player, computer)

    return result