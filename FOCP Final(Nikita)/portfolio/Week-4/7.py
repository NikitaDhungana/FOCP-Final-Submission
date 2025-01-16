'''
Write a program that reads 6 temperatures (in the same format as before), and
displays the maximum, minimum, and mean of the values.
Hint: You should know there are built-in functions for max and min. If you hunt, you
might also find one for the mean.
'''

def Tem():
    print("Enter 6 temperatures:")
    temperatures=[]
    for x in range (6):
        temp=float(input(f"temperatures {x+1}:"))
        temperatures.append(temp)
    mx=max(temperatures)
    mi=min(temperatures)
    me=sum(temperatures) / len(temperatures)    
    print("maximum temperatures",mx)
    print("minimum temperatures",mi)
    print("mean of temperatures",me)
Tem()    