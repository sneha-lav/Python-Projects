from slot_machine import spin, payout

balance = 500

print("=" * 40)
print("        🎰 LUCKY SPIN 🎰")
print("=" * 40)

while balance > 0:

    print(f"\nCurrent Balance: ${balance}")

    while True:
        try:
            bet = int(input("Enter your bet: $"))

            if 0 < bet <= balance:
                break

            print("Invalid bet.")

        except ValueError:
            print("Enter a valid number.")

    balance -= bet

    print("\n🎰 Spinning...\n")

    result = spin()

    print(" | ".join(result))

    winnings = payout(result, bet)

    if winnings:

        print(f"\n🎉 You won ${winnings}!")

        balance += winnings

    else:
        print("\n😔 Better luck next time!")

    print(f"Balance: ${balance}")

    again = input("\nSpin again? (Y/N): ").lower()

    if again != "y":
        break

print("\nThanks for playing Lucky Spin! 👋")