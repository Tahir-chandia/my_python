"""
Problem Statement
-----------------

Simulate rolling two dice, three times.
Prints the results of each die roll.
This program is used to show how variable scope works."""


import random # import random  liabraryu to use random nubers 

NUM_SIDES = 6 # Constant number
def roll_dice(): # Dice function
    """
    Simuale rolling two dice and print their total
    """
    die1:int= random.randint(1,NUM_SIDES) # Dice 1 with random numbers between 1 to 6 
    die2:int= random.randint(1,NUM_SIDES) # Dice 2 with random numbers between 1 to 6
    total:int= die1+ die2  # Sum the numbers of die1 and die2
    print(f"Total of two dices is {str(total)}")  # Print the total of die1 and die2


def main():
    die1: int = 10  # main die
    print("die1 in main() starts as: " + str(die1))
    roll_dice()  # Call roll_dice to get first result
    roll_dice()  # Call roll_dice to second result
    roll_dice()  # Call roll_dice to get third result
    print("die1 in main() is: " + str(die1))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()