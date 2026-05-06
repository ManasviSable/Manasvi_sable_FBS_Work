# Function to add two numbers
def addition(num1, num2):
    return num1 + num2
# Example usage
result = addition(5, 3) 
print("The sum is:", result)

#addition for given range
def addition_range(start, end):
    total = 0
    for num in range(start, end + 1):
        total += num
    return total
# Example usage
range_sum = addition_range(1, 10)   
print("The sum of numbers from 1 to 10 is:", range_sum)