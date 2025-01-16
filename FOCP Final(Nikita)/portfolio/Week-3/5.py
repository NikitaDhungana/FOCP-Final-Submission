'''
Modify your program a final time so that it executes until the user successfully
chooses a password. That is, if the password chosen fails any of the checks, the
program should return to asking for the password the first time.
'''

def set_password():
    BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
    print("Set a new password.")
    print("Password must be between 8 and 12 characters.")
    print("Password must not be one of the common passwords:", BAD_PASSWORDS)
    while True:  
        password1 = input("\nEnter your password: ")
        if len(password1) < 8 or len(password1) > 12:
            print("Error: Password must be between 8 and 12 characters. Please try again.")
            continue
        if password1.lower() in BAD_PASSWORDS:
            print("Error: Password is too common. Please choose a more secure password.")
            continue
        password2 = input("Confirm your password: ")
        if password1 == password2:
            print("Password Set!")
            break 
        else:
            print("Error: Passwords do not match. Please try again.")

set_password()
