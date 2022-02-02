#prime number
num = int(input("Enter a number:"))

for i in range(2,int((num/2)+1)):
    if num%i==0:
        print("This is not a prime numer")
        break
else:
    print("This is a prime number")
