import random

def get_settings(choice):
    if choice == "1":
        return 50, 10
    elif choice == "2":
        return 100, 7
    elif choice == "3":
        return 500, 10
    return None


def hint(secret, guess):
    difference = abs(secret - guess)

    if difference <= 5:
        print("🔥 You're very close!")
    elif difference <= 15:
        print("🌡️ You're close!")
    elif difference <= 30:
        print("🙂 You're getting warmer!")
    else:
        print("❄️ You're far away.")


def play_game(max_number, attempts):

    secret = random.randint(1, max_number)

    for attempt in range(1, attempts + 1):

        print(f"\nAttempt {attempt}/{attempts}")

        while True:
            try:
                guess = int(input("Enter your guess: "))
                break
            except ValueError:
                print("Please enter a valid number.")

        if guess == secret:
            print("\n🎉 Congratulations!")
            print(f"You guessed the number in {attempt} attempts!")

            stars = max(1, 6 - attempt)

            print("⭐" * stars)

            return

        elif guess > secret:
            print("⬆️ Too High")
        else:
            print("⬇️ Too Low")

        hint(secret, guess)

        print(f"Attempts Left: {attempts - attempt}")

    print("\n😔 Game Over!")
    print(f"The secret number was {secret}.")