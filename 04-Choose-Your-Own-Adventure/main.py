from story import start

while True:

    start()

    again = input("\nPlay Again? (Y/N): ").lower()

    if again != "y":
        print("\nThanks for playing!")
        break