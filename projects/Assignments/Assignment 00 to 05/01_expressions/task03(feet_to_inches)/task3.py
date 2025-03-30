INCHES_IN_FOOT:int =12 # 12 inches per foot

def main():
    #Get the number of feet in float
    inches_in_feet:float = float(input("Enter number of feet "))
    # Perform the conversion
    inches:float =INCHES_IN_FOOT * inches_in_feet
    # Print answere of the conversion
    print("That is", inches , "inches! " )


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()