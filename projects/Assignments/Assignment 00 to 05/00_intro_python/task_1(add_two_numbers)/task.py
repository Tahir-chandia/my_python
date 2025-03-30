def main():
    name:str = input("Enter your name: ")
    print(f"Welcome! {name} to python program this program add two numbers: ")
    num1:str =input("Enter your first number: ") # Get user first input
    intnum1:int =int(num1) # Read user input and convert it to integer by explicit type casting
    num2:str =input("Enter your second number: ")# Get user second input
    intnum2:int =int(num2) # Read user input and convert it to integer by explicit type casting
    addnumbers:int = intnum1 + intnum2 #Add user input as integer
    print(f"The sum of {num1} and {num2} is {addnumbers}. ")  # print user input


if __name__ == "__main__" :
    main()   