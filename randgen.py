import random, pyperclip, secrets

def main():
    selections = {
        "1": "ABCDEFGHIJKLMNOPQRSTUVWXYZ", # Uppercase
        "2": "abcdefghijklmnopqrstuvwxyz", # Lowercase
        "3": "1234567890", # Numbers
        "4": "-_", # Seperators
        "5": "!@#$%^&*():<>?/.,[]" # Special Characters
    }
    
    while True:
        retrieved = input("Please enter the length of password required: ")
        try:
            length = int(retrieved)
            break
        except ValueError:
            print("Error - the length entered not an integer, please try again.")
    
    print("Please enter the requirements of the password. One character represents one type of requirement.")
    print(" 1 - Uppercase \n 2 - Lowercase \n 3 - Numbers \n 4 - Seperators \n 5 - Special Characters")

    while True:
        requirements = input("Requirements: ")
        invalidReqs = [char for char in requirements if char not in "12345"]
        if len(invalidReqs) == 0:
            chars = ''.join([selections[char] for char in requirements])
            break
        else:
            print("Error - invalid requirements, please try again.")
    
    password = ''.join(secrets.choice(chars) for _ in range(length))
    pyperclip.copy(password)
    print(f"The password generated is: {password}, password copied to clipboard for future use.")

if __name__ == "__main__":
    main()