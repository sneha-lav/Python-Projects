from getpass import getpass


def add_password():
    website = input("Website : ").strip()
    username = input("Username: ").strip()
    password = getpass("Password: ")

    if not website or not username or not password:
        print("\n❌ All fields are required.\n")
        return

    with open("passwords.txt", "a") as file:
        file.write(f"{website}|{username}|{password}\n")

    print("\n✅ Password saved successfully!\n")


def view_passwords():

    try:
        with open("passwords.txt", "r") as file:

            passwords = file.readlines()

            if not passwords:
                print("\nNo passwords saved yet.\n")
                return

            print("\n" + "=" * 50)
            print("Saved Passwords")
            print("=" * 50)

            for line in passwords:
                website, username, password = line.strip().split("|")

                print(f"🌐 Website : {website}")
                print(f"👤 Username: {username}")
                print(f"🔑 Password: {password}")
                print("-" * 50)

    except FileNotFoundError:
        print("\nNo password database found.\n")