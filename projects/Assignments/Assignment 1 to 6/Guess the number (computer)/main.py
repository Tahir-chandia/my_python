import random

def guess(x):
    number:int = int(random.randint(1,x))
    guess:int = 0
    while guess != number:
        guess:int = int(input("Enter a number: "))
        if guess < number:
            print("Sorry! Try again, Too low. ")
        elif guess > number:
            print("Sorry! Try again, Too High. ")
            
    print(f"Yes! You guess the right number computer number is {str(number)}")

guess(10)
