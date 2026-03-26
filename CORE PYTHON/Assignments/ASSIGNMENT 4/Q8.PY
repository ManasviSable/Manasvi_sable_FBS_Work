#WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

for num in range(start, end + 1):
    if num % 7 == 0 and num % 5 == 0:
        print(num, "is divisible by 7 and multiple of 5.")
        continue