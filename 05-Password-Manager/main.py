from manager import add_password, view_passwords


def menu():

    while True:

        print("=" * 45)
        print("           🔐 PASSWORD VAULT")
        print("=" * 45)

        print("""
1. Add Password
2. View Passwords
3. Exit
""")

        choice = input("Choose an option: ")

        if choice == "1":
            add_password()

        elif choice == "2":
            view_passwords()

        elif choice == "3":
            print("\nThank you for using Password Vault! 👋")
            break

        else:
            print("\n❌ Invalid option. Please try again.\n")


if __name__ == "__main__":
    menu()