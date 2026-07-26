import random
from questions import categories

def ask_questions(question_list):
    score = 0

    random.shuffle(question_list)

    for question, answer in question_list[:5]:
        print("\n" + "-" * 50)
        print(question)

        user_answer = input("Your Answer: ").strip().lower()

        if user_answer == answer:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect!")
            print(f"Correct Answer: {answer.title()}")

        print(f"Current Score: {score}")

    return score


def performance(score):
    percentage = (score / 5) * 100

    print("\n" + "=" * 50)
    print("🎉 QUIZ COMPLETE!")
    print("=" * 50)

    print(f"Final Score : {score}/5")
    print(f"Percentage  : {percentage:.0f}%")

    if percentage == 100:
        print("🏆 Outstanding! Perfect score!")
    elif percentage >= 80:
        print("🌟 Excellent work!")
    elif percentage >= 60:
        print("👏 Good job!")
    elif percentage >= 40:
        print("🙂 Keep practicing!")
    else:
        print("💪 Better luck next time!")


while True:

    print("\n" + "=" * 50)
    print("🌟      ULTIMATE TRIVIA QUIZ      🌟")
    print("=" * 50)

    print("""
Choose a Category

1. 💻 Technology
2. 🎬 Movies
3. 🌍 Geography
4. 🎲 Random
5. Exit
""")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Thanks for playing!")
        break

    if choice == "4":
        all_questions = []
        for q in categories.values():
            all_questions.extend(q)
        score = ask_questions(all_questions)

    elif choice in categories:
        score = ask_questions(categories[choice])

    else:
        print("Invalid Choice!")
        continue

    performance(score)

    again = input("\nPlay Again? (Y/N): ").lower()

    if again != "y":
        print("\nThank you for playing! 👋")
        break
