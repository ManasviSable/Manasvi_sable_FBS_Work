#WAP to calculate selling price of book based on cost price and discount.
cost = int(input("Enter cost price of book:"))
discount = int(input("Enter discount percentage:"))
selling_price = cost - (cost * discount / 100)
print("Selling price of book is:", selling_price)
