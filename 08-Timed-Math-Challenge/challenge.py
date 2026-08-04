import random
import time


def get_settings(choice):
    if choice == "1":
        return 10, ["+", "-"]
    elif choice == "2":
        return 25, ["+", "-", "*"]
    elif choice == "3":
        return 50, ["+", "-", "*"]

    return None


def generate_question(max_num, operators):

    num1 = random.randint(1, max_num)
    num2 = random.randint(1, max_num)
    operator = random.choice(operators)

    if operator == "+":
        answer = num1 + num2
    elif operator == "-":
        answer = num1 - num2
    else:
        answer = num1 * num2

    return num1, num2, operator, answer


def play_game(max_num, operators):

    score = 0
    total_time = 0

    for question in range(1, 11):

        num1, num2, operator, answer = generate_question(max_num, operators)

        print(f"\nQuestion {question}/10")

        start = time.time()

        while True:
            try:
                guess = int(input(f"{num1} {operator} {num2} = "))
                break
            except ValueError:
                print("Please enter a number.")

        elapsed = time.time() - start
        total_time += elapsed

        if guess == answer:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect! Answer: {answer}")

        print(f"Time: {elapsed:.2f} seconds")

    return score, total_time