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
        else:
            print("Incorrect password.")
    else:
        print("Username not found. Please sign up first.")

def main():
    users_db = {}  # Dictionary to store user credentials
    while True:
        print("\n1. Login\n2. Sign Up\n3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            login(users_db)
        elif choice == "2":
            sign_up(users_db)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
