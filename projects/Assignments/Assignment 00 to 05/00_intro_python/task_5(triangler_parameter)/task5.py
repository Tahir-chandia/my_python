def main():
    # Get the input from user fot three sides of triangle
    side1:float=float(input("What is the length of side1? "))
    side2:float=float(input("What is the length of side2? "))
    side3:float=float(input("What is the length of side3? "))

    # Print and sum all the sides of triangle
    print("The parameter of triangle is " + str(side1 + side2 +side3) )


if __name__ == "__main__":
    main()