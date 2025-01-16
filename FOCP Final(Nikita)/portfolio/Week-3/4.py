'''
Modify your program again so that the chosen password cannot be one of a list of
common passwords, defined thus:
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
'''

def set_password():
    BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
    print("Set a new password. (Password must be between 8 and 12 characters and not a common password.)")
    while True: 
        password1 = input("Enter your password: ")
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
