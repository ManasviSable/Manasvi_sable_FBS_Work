#WAP to print all integers upto n that aren’t divisible by 2 and 3.
n = int(input("Enter a number:"))
for i in range(2,4):
    for j in range(1,n+1):
        if j % i != 0:
            print(j, "is not divisible by", i)
            continue
