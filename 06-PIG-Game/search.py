def binary_search(numbers, target):

    left = 0
    right = len(numbers) - 1
    steps = 0

    while left <= right:

        middle = (left + right) // 2
        steps += 1

        print(f"Checking index {middle} → {numbers[middle]}")

        if numbers[middle] == target:
            return middle, steps

        elif numbers[middle] < target:
            left = middle + 1

        else:
            right = middle - 1

    return -1, steps