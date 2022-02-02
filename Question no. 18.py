Below = int(input("Find sum of prime numbers below : "))

sum = 0

for num in range(2, Below + 1):

    i = 2
    
    for i in range(2, num):
        if (int(num % i) == 0):
            i = num
            break;

    #If the number is prime then add it.
    if i is not num:
        sum += num

print("\nSum of all prime numbers upto", Below, ":", sum)
