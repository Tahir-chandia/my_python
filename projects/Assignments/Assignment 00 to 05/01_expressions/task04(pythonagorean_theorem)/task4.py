import math #import math liabrary to use sqrt()

def main():
    
    ab:float = float(input("Enter the length of AB: "))
    ac:float = float(input("Enter the length of AC: "))
    # Calculate BC(the hypothenuse) by using this formula BC ** 2 =AB ** 2 + AC**2
    bc:float = math.sqrt(ab ** 2 + ac ** 2)
    print(f"The length of BC (the hypotenuse) is: {bc}")

if __name__ =="__main__":
    main()