def main():
     # Get the numbers we want to divide
    divided_by:int = int(input("Please enter an integer to be divided: "))
    divide_by:int = int(input("Please enter an integer to divide by : "))

    quotient:int = divided_by // divide_by # Divide with no remainder/decimals (integer division)
    remainder:int=  divide_by % divided_by # Get the remainder of the division (modulo)

    print(f"The result of this division is {str(quotient)} with a remainder of {str(remainder)} ")

if __name__ == "__main__":
    main()