def set_activities():
    activities = {}
    print("Welcome to the Activity Scheduler!")
    print("You can schedule up to 5 activities for free.")
    
    while len(activities) < 5:
        activity = input("Enter an activity (or type 'done' to finish): ")
        if activity.lower() == "done":
            break
        time = input(f"Set a time for '{activity}' (e.g., HH:MM): ")
        activities[activity] = time
        print(f"Activity '{activity}' scheduled at {time}.")

    if len(activities) == 5:
        print("You’ve reached the limit of 5 activities. Upgrade to premium to add more.")
    
    print("\nYour activities:")
    for act, time in activities.items():
        print(f"{act} at {time}")

if __name__ == "__main__":
    set_activities()
