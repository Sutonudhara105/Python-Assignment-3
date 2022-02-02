pr = ""; comp = ""
c=0
while True:
    c+=1
    n = input("Enter a number ")
    m = int(n)
    if m == -1:
        break
    flag=0
    for i in range(2,m):
        if m % i == 0:
            flag=1
            break
    if flag==0:
        pr = pr + n + ","
    else:
        comp = comp + n + ","
    if c > 1:
        print("If you don't want to continue, type -1")

print(f"Prime numbers are: {pr}")
print(f"Composite numbers are: {comp}")

