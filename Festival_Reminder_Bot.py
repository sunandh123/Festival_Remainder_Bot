import datetime
import time
from plyer import notification

# Dictionary to store festivals
festivals = {
    "Diwali": "2025-10-20",
    "Christmas": "2025-12-25",
    "New Year": "2026-01-01"
}

# Add or edit a festival
def add_festival():
    name = input("Enter festival name: ")
    date_str = input("Enter festival date (YYYY-MM-DD): ")
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        festivals[name] = date_str
        print("Festival added/updated successfully.")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

# Check for today's festivals
def check_festivals():
    today = datetime.date.today().strftime("%Y-%m-%d")
    for name, date in festivals.items():
        if date == today:
            notification.notify(
                title="Festival Reminder",
                message=f"Today is {name}!",
                timeout=10
            )
            print(f"Reminder: Today is {name}")

# Main loop
while True:
    print("\n1. View Festivals\n2. Add/Edit Festival\n3. Check Today's Festivals\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        if festivals:
            for name, date in festivals.items():
                print(f"{name} - {date}")
        else:
            print("No festivals added yet.")
    elif choice == "2":
        add_festival()
    elif choice == "3":
        check_festivals()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice.")

    time.sleep(1)