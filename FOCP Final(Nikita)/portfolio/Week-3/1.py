'''
Modify your greeting program so that if the user does not enter a name (i.e. they
just press enter), the program responds "Hello, Stranger!". Otherwise it should print
a greeting with their name as before.
'''

def greet_user():
    name = input("Enter your name: ")
    if name:  
        print(f"Hello, {name}!")
    else:  
        print("Hello, Stranger!")
greet_user()
