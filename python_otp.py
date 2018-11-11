"""One-time-password demo by Martin Soovali."""
import pyotp
import os


def cls():
    """Clear console screen (clear if unix, cls if Windows)."""
    os.system('cls' if os.name == 'nt' else 'clear')


def generate_key():
    """Generate base32 encoded key using pyotp module."""
    return pyotp.random_base32()


def get_onetime_password(key):
    """Return 6 digit one-time-password based on base32 encoded string."""
    totp = pyotp.totp.TOTP(key)
    return totp.now()


if __name__ == '__main__':
    condition = 0
    secret_key = "Secret key has not been generated yet!\n"
    while condition == 0:
        print("Select option:\n"
              "a) Generate key\n"
              "b) Show key\n"
              "c) Generate OTP with generated key\n"
              "e) Exit\n")
        selection = input()
        if selection in "Aa":
            secret_key = generate_key()
            cls()
            print("\n")
            print("Key has been generated!\n")
        elif selection in "Bb":
            cls()
            print("\n")
            print(secret_key)
        elif selection in "Cc":
            cls()
            print("\n")
            if secret_key == "Secret key has not been generated yet!\n":
                print(secret_key)
            else:
                print(get_onetime_password(secret_key))
        elif selection in "Ee":
            print("Have a great day!\n")
            exit()
        else:
            cls()
            print("\nWrong choice! Try again.\n")
