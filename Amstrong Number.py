#Amstrong Number
num=int(input("Enter a number"))
temp=num
sum=0
while temp>0:
    rem=temp%10
    sum=sum+rem**3
    temp//=10


if num==sum:
    print("This is an armstrong number")    
else:
    print("this is not a armstrong number")
