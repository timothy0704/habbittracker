def sign_up(users_db):
    username = input("Enter a new username: ")
    if username in users_db:
        print("Username already exists. Try another.")
    else:
        password = input("Enter a new password: ")
        users_db[username] = password
        print("Sign-up successful!")

def login(users_db):
    username = input("Enter username: ")
    if username in users_db:
        password = input("Enter password: ")
        if users_db[username] == password:
            print("Login successful!")
            return username
        else:
            print("Incorrect password.")
    else:
        print("Username not found. Please sign up first.")
    return None

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
    users_db = {}  # Dictionary to store user credentials
    while True:
        print("\n1. Login\n2. Sign Up\n3. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            user = login(users_db)
            if user:
                premium = False
                if input("Upgrade to premium for $5/month? (yes/no): ").lower() == "yes":
                    input("Press Enter to confirm payment...")
                    print("Thank you! Premium activated.")
                    premium = True
                set_activities(premium)
        elif choice == "2":
            sign_up(users_db)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
