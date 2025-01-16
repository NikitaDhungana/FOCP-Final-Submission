'''
Write and test a function that converts a temperature measured in degrees
centigrade into the equivalent in fahrenheit, and another that does the reverse
conversion. Test both functions. (Google will find you the formulae).
'''

def tempf(temp):
    f=(temp*9/5)+32
    print("Temperature in fahrenheit is:", f)
def tempc(temp):
    c=(temp-32)*5/9
    print("Temperature in celsius is:", c)
check=input("Which one do you choose,(f/c)?").lower
temp = float(input("Enter the temperature: "))
if check == "c":
    tempf(temp)
else:
    tempc(temp)