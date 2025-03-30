import random
NUM_ROUND:int = 3
def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    num = 0
    round = 1
    your_score:int = 0

    while num < NUM_ROUND:    
        print("Round ",round)
        my_num:int =int(input("Your number is: "))
        computer_num:int = random.randint(1,100) 
        choice:str = input("Do you think your number is higher or lower than the computer's?: ")
        print(f"Your number is {str(my_num)}")
        print(choice)
        if choice=="higher" and my_num > computer_num :
            print("You win! ")
            your_score += 1
            print("You win! ")
            print(f"Your score is {your_score} ")
            print(f"You were right! The computer's number was {computer_num}\n")
        elif choice == "higher" and my_num < computer_num:
            print("Computer wins! ")
            print(f"Aww, that's incorrect. The computer's number was {computer_num}\n")
        elif choice == "lower" and my_num > computer_num:
            print("Computer wins! ")
            print(f"Aww, that's incorrect. The computer's number was {computer_num}\n")
        elif choice == "lower" and my_num < computer_num:
            print("You wins! ")
            your_score += 1
            print(f"Your score is {your_score} ")
            print(f"You were right! The computer's number was {computer_num}\n")
        elif choice :
            print("Computer Wins!")
            print(f"Aww, that's incorrect. The computer's number was {computer_num}\n")
        num+=1
        round +=1
    print(f"Your total score is: {your_score}")
    print("Thanks for playing! ")

if __name__ == "__main__":
    main()