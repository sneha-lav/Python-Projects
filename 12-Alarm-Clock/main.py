from alarm import start_alarm, validate_time

while True:

    print("=" * 45)
    print("            ⏰ WAKEUP")
    print("=" * 45)

    alarm = input("Enter alarm time (HH:MM): ")

    if not validate_time(alarm):
        print("\n❌ Invalid time format.\n")
        continue

    start_alarm(alarm)

    again = input("\nSet another alarm? (Y/N): ").lower()

    if again != "y":
        print("\nGoodbye! 👋")
        break