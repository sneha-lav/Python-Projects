from quotes import get_quote
from typing_test import start_test

while True:

    print("=" * 45)
    print("          ⌨️ TYPERUSH")
    print("=" * 45)

    sentence = get_quote()

    elapsed, wpm, accuracy = start_test(sentence)

    print("\n" + "=" * 45)
    print("RESULTS")
    print("=" * 45)

    print(f"Time Taken : {elapsed:.2f} seconds")
    print(f"WPM        : {wpm:.0f}")
    print(f"Accuracy   : {accuracy:.2f}%")

    if accuracy == 100:
        print("🏆 Perfect Accuracy!")

    elif accuracy >= 90:
        print("🌟 Excellent!")

    elif accuracy >= 75:
        print("👏 Great Job!")

    else:
        print("💪 Keep Practicing!")

    again = input("\nTry another quote? (Y/N): ").lower()

    if again != "y":
        print("\nThanks for using TypeRush! 👋")
        break