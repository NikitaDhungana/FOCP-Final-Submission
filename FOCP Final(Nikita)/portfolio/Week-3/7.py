'''
Modify your "Times Table" program so that the user enters the number of the table
they require. This number should be between 0 and 12 inclusive.
'''

def times_table():
    while True: 
        try:
            table = int(input("Enter the number for the times table (0-12): "))
            if 0 <= table <= 12:
                break 
            else:
                print("Error: Please enter a number between 0 and 12.")
        except ValueError:
            print("Error: Please enter a valid integer.")
    print("f\n{table} Times Table:")
    for i in range(13): 
        print(f"{i} x {table} = {i * table}")
times_table()
