import random

def main():
    print("Guess the number: ")
    print("I am thinking of a number between 0 and 99...")
    number:int = int(input("Enter a guess: "))

    
    for num in range(number,100):
        num:int = random.randint(1,num)

    while True:
        if num == number:
            print(f"Congrats! The number was: {num}")
            break
        elif num > number:
            print("Your guess is too low")
            number:int = int(input("Enter a new number: "))
        elif num < number:
            print("Your guess is too High")
            number:int = int(input("Enter a new number: "))

if __name__ == "__main__":
    main()