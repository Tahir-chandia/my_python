def main():
    year:int = int(input("Please enter year to check it is leap year or not. "))

    if year % 4 ==0:  # Checking whether the provided year is evenly divisibly by 4
        if year % 100 == 0:  # Checking whether the provided year is evenly divisibly by 40
            if year % 400 ==0:  # Checking whether the provided year is evenly divisibly by 400
                print("That's leap year. ")
            else:# (Not divisible by 400)
                print("That' not leap year. ")
        else:# (Not divisible by 100)
            print("That's leap year. ")
    else:# (Not divisible by 4)
        print("That's not leap year. ")

if __name__ == "__main__":
        main()


