from generator import generate_password

while True:

    print("=" * 45)
    print("         🔐 SECUREPASS")
    print("=" * 45)

    while True:
        try:
            length = int(input("Password Length: "))

            if length >= 4:
                break

            print("Password should be at least 4 characters.")

        except ValueError:
            print("Enter a valid number.")

    upper = input("Include Uppercase? (Y/N): ").lower() == "y"
    lower = input("Include Lowercase? (Y/N): ").lower() == "y"
    digits = input("Include Numbers? (Y/N): ").lower() == "y"
    symbols = input("Include Special Characters? (Y/N): ").lower() == "y"

    password = generate_password(length, upper, lower, digits, symbols)

    if password:
        print("\nGenerated Password:")
        print(password)
    else:
        print("\nSelect at least one character type.")

    again = input("\nGenerate another password? (Y/N): ").lower()

    if again != "y":
        print("\nThank you for using SecurePass! 👋")
        break