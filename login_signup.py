def display_menu():
    print("1. Login")
    print("2. Sign Up")
    print("3. Delete Account")
    print("4. Edit Account")
    print("5. Search Account")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    return choice

def login(users):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username] == password:
        print("Login successful!")
    else:
        print("Invalid username or password.")

def sign_up(users):
    username = input("Enter a new username: ")
    if username in users:
        print("Username already exists. Please choose a different one.")
        return

    password = input("Enter a password: ")
    users[username] = password
    print("Sign up successful!")

def delete_account(users):
    username = input("Enter the username you want to delete: ")
    if username in users:
        del users[username]
        print("Account deleted successfully.")
    else:
        print("Username not found.")

def edit_account(users):
    username = input("Enter the username you want to edit: ")
    if username in users:
        new_password = input("Enter the new password: ")
        users[username] = new_password
        print("Account updated successfully.")
    else:
        print("Username not found.")

def search_account(users):
    username = input("Enter the username you want to search for: ")
    if username in users:
        print(f"Username: {username}, Password: {users[username]}")
    else:
        print("Username not found.")

def main():
    users = {}  # Dictionary to store username-password pairs

    while True:
        choice = display_menu()

        if choice == 1:  # Login
            login(users)
        elif choice == 2:  # Sign Up
            sign_up(users)
        elif choice == 3:  # Delete Account
            delete_account(users)
        elif choice == 4:  # Edit Account
            edit_account(users)
        elif choice == 5:  # Search Account
            search_account(users)
        elif choice == 6:  # Exit
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()