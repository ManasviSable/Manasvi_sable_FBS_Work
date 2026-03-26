#WAP to print Fibonacci series upto n.
n = int(input("Enter a number: "))
a, b = 0, 1
print("Fibonacci series upto", n, "is:")
while a <= n:
    print(a)
    a, b = b, a + b
    