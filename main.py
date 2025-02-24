from encryption import load_key, encrypt_password, decrypt_password
from storage import save_password, retrieve_password

def main():
    key = load_key()  # Load or generate an encryption key

    while True:
        print("\nPassword Manager")
        print("1. Save a new password")
        print("2. Retrieve a password")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            website = input("Enter website/app name: ")
            username = input("Enter username/email: ")
            password = input("Enter password: ")
            encrypted_password = encrypt_password(password, key)
            save_password(website, username, encrypted_password)
            print("Password saved successfully!")

        elif choice == "2":
            website = input("Enter website/app name: ")
            username, encrypted_password = retrieve_password(website)
            if encrypted_password:
                decrypted_password = decrypt_password(encrypted_password, key)
                print(f"Username: {username}")
                print(f"Password: {decrypted_password}")
            else:
                print("No password found for this website.")

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
