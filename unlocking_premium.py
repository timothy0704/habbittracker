def set_activities(premium=False):
    activities = {}
    print("Welcome to the Activity Scheduler!")
    print("You can schedule up to 5 activities for free.")
    
    while len(activities) < (5 if not premium else float('inf')):
        activity = input("Enter an activity (or type 'done' to finish): ")
        if activity.lower() == "done":
            break
        time = input(f"Set a time for '{activity}' (e.g., HH:MM): ")
        activities[activity] = time
        print(f"Activity '{activity}' scheduled at {time}.")

        if not premium and len(activities) == 5:
            print("You’ve reached the limit. Upgrade to premium to add more.")
            break
    
    print("\nYour activities:")
    for act, time in activities.items():
        print(f"{act} at {time}")

def main():
    premium = False
    if input("Upgrade to premium for $5/month? (yes/no): ").lower() == "yes":
        input("Press Enter to confirm payment...")
        print("Thank you! Premium activated.")
        premium = True
    
    set_activities(premium)

if __name__ == "__main__":
    main()
