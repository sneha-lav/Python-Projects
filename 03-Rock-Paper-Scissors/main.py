from game import play_round

wins = 0
losses = 0
draws = 0

while True:

    print("\n" + "=" * 40)
    print("     ✊ ROCK PAPER SCISSORS ✂️")
    print("=" * 40)

    result = play_round()

    if result == "Win":
        wins += 1
        print("\n🎉 You Win!")

    elif result == "Lose":
        losses += 1
        print("\n😔 You Lose!")

    else:
        draws += 1
        print("\n🤝 It's a Draw!")

    print("\nScoreboard")
    print("-" * 20)
    print(f"Wins   : {wins}")
    print(f"Losses : {losses}")
    print(f"Draws  : {draws}")

    again = input("\nPlay Again? (Y/N): ").lower()

    if again != "y":
        print("\nThanks for playing! 👋")
        break