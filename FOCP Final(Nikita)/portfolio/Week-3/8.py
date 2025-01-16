'''
Modify the "Times Table" again so that the user still enters the number of the table,
but if this number is negative the table is printed backwards. So entering "-7"
would produce the Seven Times Table starting at "12 times" down to "0 times".
'''

def times_table():
    while True: 
        try:
            table = int(input("Enter the number for the times table (0-12, or negative for reverse): "))
            if -12 <= table <= 12:
                break 
            else:
                print("Error: Please enter a number between -12 and 12.")
        except ValueError:
            print("Error: Please enter a valid integer.")
    
    abs_table = abs(table)  
    if table < 0:
        print(f"\n{abs_table} Times Table (Backwards):")
        for i in range(12, -1, -1):  
            print(f"{i} x {abs_table} = {i * abs_table}")
    else:
        print(f"\n{table} Times Table:")
        for i in range(13): 
            print(f"{i} x {table} = {i * table}")
times_table()
