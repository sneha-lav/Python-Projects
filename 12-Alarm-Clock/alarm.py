from datetime import datetime
import time
from playsound import playsound


def validate_time(alarm_time):
    try:
        datetime.strptime(alarm_time, "%H:%M")
        return True
    except ValueError:
        return False


def start_alarm(alarm_time):

    print("\n⏰ Alarm set successfully!")

    while True:

        current_time = datetime.now().strftime("%H:%M:%S")

        print(f"\rCurrent Time: {current_time}", end="")

        if current_time[:5] == alarm_time:

            print("\n\n🔔 WAKE UP!")

            playsound("sound.mp3")

            break

        time.sleep(1)