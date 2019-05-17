import random
import pyperclip

def main():
    uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    lowercase = [letter.lower() for letter in uppercase]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    seperator = [" ", "-", "_"]
    specialChars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", ":", "<", ">", "?", "/"]
    length = 0
    requirement = ""
    password = ""
    selectedList = []
    
    while (length == 0):
        retrieved = input("Please enter the length of password required: ")
        try:
            length = int(retrieved)
        except ValueError:
            print("Error - not an integer.")
    
    print("Please enter the requirements of the password. One character represents one type of requirement.")
    print(" 1 - Uppercase \n 2 - Lowercase \n 3 - Numbers \n 4 - Seperators \n 5 - Special Characters")

    while (requirement == ""):
        answer = input("Requirements: ")
        if checkReq(answer):
            requirement = answer
        else:
            print("Invalid requirements, please try again.")
    
    for c in requirement:
        if c == "1": 
            selectedList += uppercase
        elif c == "2":
            selectedList += lowercase
        elif c == "3":
            selectedList += numbers
        elif c == "4":
            selectedList += seperator
        elif c == "5":
            selectedList += specialChars
    
    for _ in range(length):
        pos = random.randint(0, len(selectedList)-1)
        password += selectedList[pos]

    print(f"The password generated is: {password}, password copied to clipboard for future use.")

    pyperclip.copy(password)

def checkReq(string):
    for letter in string:
        if letter not in ["1", "2", "3", "4", "5"]:
            return False
    return True

if __name__ == "__main__":
    main()