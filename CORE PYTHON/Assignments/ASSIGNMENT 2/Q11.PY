#Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.
amount = int(input("Enter an amount:"))
notes_2000 = amount // 2000
amount = amount % 2000
notes_500 = amount // 500
amount = amount % 500
notes_100 = amount // 100
amount = amount % 100
notes_50 = amount // 50
amount = amount % 50
notes_20 = amount // 20
amount = amount % 20
notes_10 = amount // 10
amount = amount % 10


print("Minimum number of notes needed:")
print("2000:", notes_2000)
print("500:", notes_500)
print("100:", notes_100)
print("50:", notes_50)
print("20:", notes_20)
print("10:", notes_10)
