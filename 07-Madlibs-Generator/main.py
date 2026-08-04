from stories import get_story

print("=" * 45)
print("        📖 STORYCRAFT")
print("=" * 45)

while True:

    print("\nLet's create a funny story!\n")

    name = input("Enter a name: ")
    place = input("Enter a place: ")
    adjective = input("Enter an adjective: ")
    animal = input("Enter an animal: ")

    story = get_story().format(
        name=name,
        place=place,
        adjective=adjective,
        animal=animal
    )

    print("\n" + "=" * 45)
    print("YOUR STORY")
    print("=" * 45)

    print(story)

    again = input("\nCreate another story? (Y/N): ").lower()

    if again != "y":
        print("\nThanks for using StoryCraft! 👋")
        break