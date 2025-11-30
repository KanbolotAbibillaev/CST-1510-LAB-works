import bcrypt
import os
USER_DATA_FILE = "users.txt"

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed.encode())

def user_exists(username):
    if not os.path.exists(USER_DATA_FILE):
        return False

    f = open(USER_DATA_FILE, "r")
    for line in f:
        data = line.strip().split(",")
        if data[0] == username:
            f.close()
            return True
    f.close()
    return False

def register_user(username, password):
    if user_exists(username):
        print("Username already exists")
        return False

    hashed = hash_password(password)

    f = open(USER_DATA_FILE, "a")
    f.write(username + "," + hashed + "\n")
    f.close()

    print("User registered")
    return True

def login_user(username, password):
    if not os.path.exists(USER_DATA_FILE):
        print(" User not found")
        return False

    f = open(USER_DATA_FILE, "r")
    for line in f:
        data = line.strip().split(",")
        if data[0] == username:
            if verify_password(password, data[1]):
                print("Login success")
                f.close()
                return True
            else:
                print("Wrong password")
                f.close()
                return False
    f.close()

    print("Username not found")
    return False

def validate_username(username):
    if len(username) < 3:
        return False, "Username too short."
    if len(username) > 20:
        return False, "Username too long."
    if not username.isalnum():
        return False, "Username must be letters and numbers."
    return True, ""

def validate_password(password):
    if len(password) < 6:
        return False, "Password too short."
    if not any(c.islower() for c in password):
        return False, "Needs lowercase letter."
    if not any(c.isupper() for c in password):
        return False, "Needs uppercase letter."
    if not any(c.isdigit() for c in password):
        return False, "Needs a number."
    return True, ""

def menu():
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")
def main():
    print("Welcome to the Auth System")
    while True:
        menu()
        choice = input("Choose: ")
        if choice == "1":
            username = input("Username: ")
            ok, msg = validate_username(username)
            if not ok:
                print(msg)
                continue
            password = input("Password: ")
            ok, msg = validate_password(password)
            if not ok:
                print(msg)
                continue
            confirm = input("Confirm password: ")
            if confirm != password:
                print("Passwords don't match.")
                continue
            register_user(username, password)
        elif choice == "2":
            username = input("Username: ")
            password = input("Password: ")
            login_user(username, password)
        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Wrong option.")

if __name__ == "__main__":
    main()