from search import binary_search

numbers = list(range(1, 101))

print("=" * 45)
print("      🔍 BINARY SEARCH VISUALIZER")
print("=" * 45)

while True:

    try:
        target = int(input("\nEnter a number (1-100): "))

        if target not in numbers:
            print("Number must be between 1 and 100.")
            continue

        index, steps = binary_search(numbers, target)

        print(f"\n✅ Number found at index {index}")
        print(f"Iterations: {steps}")

        again = input("\nSearch again? (Y/N): ").lower()

        if again != "y":
            print("\nThanks for using Binary Search Visualizer! 👋")
            break

    except ValueError:
        print("Please enter a valid integer.")