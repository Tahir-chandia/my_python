def get_list():
    my_list:list[str] = [] # Make an empty list to store values
    elements:str = input("Please enter a value. ") # Get an initial value
    while elements != "":
        my_list.append(elements) # Add values to the list
        elements:str = input("Please enter a value. ") # Get next value
    return my_list

def main():

   li= get_list()
   print("Here's the list ",li)

if __name__== "__main__":
    main()
