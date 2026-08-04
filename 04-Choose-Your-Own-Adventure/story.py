def start():

    print("\n🏛️ Echoes of the Forgotten Temple\n")

    print("While exploring an old jungle, you discover a forgotten temple.")
    print("Its massive stone doors slowly begin to open...\n")

    choice = input("Do you ENTER or LEAVE? ").lower()

    if choice == "enter":
        temple()

    elif choice == "leave":
        print("\n🕊️ You decide some mysteries are better left untouched.")
        print("Ending Unlocked: The Safe Escape")

    else:
        print("\nInvalid choice.")


def temple():

    print("\nInside the temple you find two paths.")

    choice = input("Go LEFT or RIGHT? ").lower()

    if choice == "left":
        treasure_room()

    elif choice == "right":
        snake_room()

    else:
        print("\nYou hesitate too long.")
        print("The temple collapses.")
        print("Ending Unlocked: Buried Alive 💀")


def treasure_room():

    print("\n✨ A room filled with gold appears before you.")
    print("A glowing treasure chest sits in the center.")

    choice = input("OPEN the chest or LEAVE it? ").lower()

    if choice == "open":
        print("\n🏆 You found the Lost King's Treasure!")
        print("Ending Unlocked: Treasure Hunter")

    elif choice == "leave":
        print("\n😊 Greed didn't control you.")
        print("Ending Unlocked: Wise Explorer")

    else:
        print("\nThe room disappears around you.")


def snake_room():

    print("\n🐍 Giant snakes surround an ancient idol.")

    choice = input("RUN or FIGHT? ").lower()

    if choice == "run":
        print("\n🏃 You escape just in time!")
        print("Ending Unlocked: Lucky Escape")

    elif choice == "fight":
        print("\n💀 The snakes overpower you.")
        print("Ending Unlocked: Snake's Revenge")

    else:
        print("\nThe snakes quietly watch you...")