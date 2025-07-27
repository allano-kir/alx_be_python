# daily_reminder.py

# Loop to ensure valid input
while True:
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").lower().strip()
    time_bound = input("Is it time-bound? (yes/no): ").lower().strip()

    # Check for valid priority
    if priority not in ["high", "medium", "low"]:
        print("Invalid priority level. Please enter high, medium, or low.")
        continue

    # Check for valid time_bound input
    if time_bound not in ["yes", "no"]:
        print("Invalid response for time-bound. Please enter yes or no.")
        continue

    # Process task based on priority using match-case
    match priority:
        case "high":
            message = f"'{task}' is a high priority task"
        case "medium":
            message = f"'{task}' is a medium priority task"
        case "low":
            message = f"'{task}' is a low priority task"
        case _:
            message = f"'{task}' has an unspecified priority"

    # Check time sensitivity
    if time_bound == "yes":
        message += " that requires immediate attention today!"
    else:
        message += ". Consider completing it when you have free time."

    # Print final reminder
    print("\nReminder:", message)
    break
