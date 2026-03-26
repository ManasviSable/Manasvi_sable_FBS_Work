#add gst in final bill
prod1 = int(input("Enter the price of 1st product:"))
prod2 =  int(input("Enter the price of 2nd product:"))
prod3 =  int(input("Enter the price of 3rd product:"))
prod4 =  int(input("Enter the price of 4th product:"))
prod5 =  int(input("Enter the price of 5th product:"))
total = prod1 + prod2 + prod3 + prod4 + prod5
Bill = total + (0.18*total)
print("The total amount of all products including gst is:",Bill)
