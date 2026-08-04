import time


def calculate_accuracy(original, typed):

    correct = 0

    for o, t in zip(original, typed):

        if o == t:
            correct += 1

    return (correct / len(original)) * 100


def start_test(sentence):

    print("\nType the following sentence:\n")
    print(sentence)

    input("\nPress ENTER to begin...")

    start = time.time()

    typed = input("\n> ")

    end = time.time()

    elapsed = end - start

    words = len(typed.split())

    wpm = (words / elapsed) * 60

    accuracy = calculate_accuracy(sentence, typed)

    return elapsed, wpm, accuracy