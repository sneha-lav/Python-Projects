from game import get_settings, play_game

while True:

    print("\n" + "=" * 40)
    print("        🎯 GUESSMASTER 🎯")
    print("=" * 40)

    print("""
Choose Difficulty

1. Easy (1-50)
2. Medium (1-100)
3. Hard (1-500)
4. Exit
""")

    choice = input("Enter your choice: ")

    if choice == "4":
        print("Thank you for playing!")
        break

    settings = get_settings(choice)

    if settings is None:
        print("Invalid choice.")
        continue

    max_number, attempts = settings

    print(f"\nGuess the number between 1 and {max_number}")

    play_game(max_number, attempts)

    again = input("\nPlay Again? (Y/N): ").lower()

    if again != "y":
        print("\nSee you next time! 👋")
        break