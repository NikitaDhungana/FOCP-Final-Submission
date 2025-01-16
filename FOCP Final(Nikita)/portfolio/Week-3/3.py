'''
Modify your previous program so that the password must be between 8 and 12
characters (inclusive) long.
'''

def set_password():
    print("Password Setup")
    while True:
        password1 = input("Enter your new password (8-12 characters): ")
        if len(password1) < 8 or len(password1) > 12:
            print("Error: Password must be between 8 and 12 characters. Please try again.")
            continue
        password2 = input("Re-enter your password: ")
        if password1 == password2:
            print("Password Set!")
            break 
        else:
            print("Error: Passwords do not match. Please try again.")
set_password()
