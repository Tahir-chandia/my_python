import random 

print("Welcome to the Password Generator!")

chars:str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVXZ12467890~!@#$^&*()_+`'

number:int = int(input("Amount of passwords to generate: "))
length:int = int(input("Enter your password length : "))

print("\nhere are your passwords: ")

for pwd in range(number):
    passwords:str = ""
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)