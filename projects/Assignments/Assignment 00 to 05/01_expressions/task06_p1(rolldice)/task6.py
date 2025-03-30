import random # import random  liabraryu to use random nubers 


NUM_SIDES:int = 6 # Constant number

def main(): # Dice function
    die1:int = random.randint(1,NUM_SIDES) # Dice 1 with random numbers between 1 to 6
    die2:int = random.randint(1,NUM_SIDES) # Dice 2 with random numbers between 1 to 6

    total:int = die1 + die2 # Sum the numbers of die1 and die2


    print("Dice have" , NUM_SIDES , "each sides"   ) # Print Dice sides
    print("First Die", die1) # Print first die
    print("Second Die", die2) # Print second die
    print("Total of two dice", total) # Print the total of die1 and die2

if __name__ == "__main__":
    main()