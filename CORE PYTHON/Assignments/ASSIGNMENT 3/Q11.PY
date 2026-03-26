#Accept age of five people and also per person ticket amount and then calculate total amount to ticket to travel for all of them based on following condition :a. Children below 12 = 30% discount b. Senior citizen (above 59) = 50% discount c. Others need to pay full.
total_amount = 0

for i in range(1, 6):
    age = int(input(f"Enter age of person {i}: "))
    ticket = int(input(f"Enter ticket amount for person: "))

    if age < 12:
        total_amount += ticket * 0.7
    elif age > 59:
        total_amount += ticket * 0.5
    else:
        total_amount += ticket

print("Total amount:", total_amount)


