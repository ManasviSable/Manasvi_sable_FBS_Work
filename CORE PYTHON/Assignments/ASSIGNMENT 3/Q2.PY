#Write a program to input any alphabet and check whether it is vowel or consonant.
alphabet = input("Enter any alphabet: ")
if alphabet in ['a', 'e', 'i', 'o', 'u']:
    print("The alphabet is a vowel.")
else:
    print("The alphabet is a consonant.")