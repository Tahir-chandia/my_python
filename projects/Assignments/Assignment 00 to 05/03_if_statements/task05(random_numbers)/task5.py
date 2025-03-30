
import random # import random liabrary to use random values
# Constant values

N_NUMBERS : int = 10
MIN_VALUE : int = 1
MAX_VALUE : int = 100

def main():
   for i in range(0,N_NUMBERS):# using loop 10 times to print 10 random numbers
    value:int = random.randint(MIN_VALUE,MAX_VALUE) # Random value between 1 to 100
    print(value) #Print values
if __name__ == '__main__':
    main()