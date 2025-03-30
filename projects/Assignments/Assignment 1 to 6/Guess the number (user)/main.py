import random

def computer_guess(x):
    low:int=1
    high:int= x
    feedback:str=""
    while feedback != "c":
        if low != high:
            guess:int = random.randint(low,high)
        else:
            guess:int = low # could also be high because  low = high
        feedback:str = input(f"Is {guess} too high (H), too low (L), or correct (C) ").lower()
        if feedback == "h":
            high = guess-1
        elif feedback == "l":
            low = guess + 1
            
            
    print(f"Yes! The computer guessed your number,  {str(guess)} correctly!")

computer_guess(500)
