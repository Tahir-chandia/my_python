def main():
    number:int = int(input("Enter number: "))
    while number < 100:
        double:int = number * 2 
        print(str(number) + " double is " + str(double))
        number += number
       
if __name__ == "__main__":
    main()