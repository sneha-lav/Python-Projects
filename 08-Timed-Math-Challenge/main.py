from challenge import get_settings, play_game

while True:

    print("=" * 45)
    print("          🧮 MATH SPRINT")
    print("=" * 45)

    print("""
Choose Difficulty

1. Easy
2. Medium
3. Hard
4. Exit
""")

    choice = input("Enter your choice: ")

    if choice == "4":
        print("Thanks for playing!")
        break

    settings = get_settings(choice)

    if settings is None:
        print("Invalid choice.\n")
        continue

    max_num, operators = settings

    score, total_time = play_game(max_num, operators)

    print("\n" + "=" * 45)
    print("RESULTS")
    print("=" * 45)

    print(f"Score       : {score}/10")
    print(f"Accuracy    : {score * 10}%")
    print(f"Total Time  : {total_time:.2f} seconds")
    print(f"Average Time: {total_time / 10:.2f} seconds")

    if score == 10:
        print("🏆 Perfect Score!")
    elif score >= 8:
        print("🌟 Excellent!")
    elif score >= 5:
        print("👏 Good Job!")
    else:
        print("💪 Keep Practicing!")

    again = input("\nPlay Again? (Y/N): ").lower()

    if again != "y":
        print("\nGoodbye! 👋")
        break