def main():
    # User enter user  name
    user_name:str=input("Enter your name: ")
    # print user name
    print(f"Welcome {user_name}! ")
    # User enter their first favourite animal name.
    favanimal:str = input("Enter your favourite animal. ")
    # print user  favourite animal name
    print(f"My favourite animal is {favanimal}. ")
    # if user want to add som,e more names then this code execute
    while True: # This start loop for user next move 
    # Ask user if he want to add more names of favourite animal names
        choose:str = input("Do you want to give your more favourite animal names? (yes/no): ")
    # if user choose yes this will execute 
        if choose =="yes":
            favanimal2:str = input("Enter your another favourite animal. ")
            print(f"My favourite animal is also {favanimal2}. ")
    # if user choose no this will execute 
        elif choose == "no":
            print(f"Thanks {user_name}. Hope you like this program. ")
            break # this will terminate  the loop

if __name__ == '__main__':
    main()