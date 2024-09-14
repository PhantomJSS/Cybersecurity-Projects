import hashlib
import getpass

data = {}

def create_account():
    user = input("Please enter the username: ")
    password = getpass.getpass("Please enter the password: ")
    hashed_pass = hashlib.sha256(password.encode()).hexdigest()
    data[user] = hashed_pass
    print("Details Saved, Account Created")

def login():
    user = input("Please enter the username: ")
    password = getpass.getpass("Please enter the password: ")
    hashed_pass = hashlib.sha256(password.encode()).hexdigest()

    if user in data.keys() and data[user] == hashed_pass:
        print("Logged in successfully")
    else:
        print("Login failed, please try again")

def main():
    while True:
        choice = input("Please select from one of the following options:\n1. Register\n2. Login\n3. Exit\nOption #: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("Invalid input, Please try again: ")

main()