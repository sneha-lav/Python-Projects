import random
import string


def generate_password(length, upper, lower, digits, symbols):

    characters = ""

    if upper:
        characters += string.ascii_uppercase

    if lower:
        characters += string.ascii_lowercase

    if digits:
        characters += string.digits

    if symbols:
        characters += string.punctuation

    if not characters:
        return None

    password = "".join(random.choice(characters) for _ in range(length))

    return password