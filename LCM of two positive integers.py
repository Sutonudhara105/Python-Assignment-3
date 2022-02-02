# LCM of two positive integers
num1=int(input("Enter 1st numer"))
num2=int(input("Enter 2nd numer"))

if(num1 > num2 ):  
    max= num1
else:
    max= num2
while(True):
    if(max % num1 == 0 and max % num2 == 0):   
        print(max)
        break
    max= max+ 1
