import random

symbols = {
    "🍒": 4,
    "🍋": 5,
    "🔔": 3,
    "⭐": 2,
    "💎": 1
}


def spin():

    pool = []

    for symbol, count in symbols.items():
        pool.extend([symbol] * count)

    return random.choice(pool), random.choice(pool), random.choice(pool)


def payout(result, bet):

    a, b, c = result

    if a == b == c:

        if a == "💎":
            return bet * 20

        elif a == "⭐":
            return bet * 10

        elif a == "🔔":
            return bet * 6

        elif a == "🍋":
            return bet * 4

        else:
            return bet * 3

    elif a == b or b == c or a == c:
        return bet * 2

    return 0