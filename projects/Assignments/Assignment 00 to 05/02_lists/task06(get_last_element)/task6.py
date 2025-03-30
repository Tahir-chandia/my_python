def get_last_element(lst):
    """ Prints the last element of the provided list. """
    print(lst[len(lst) - 1])

# The line below works too!!
# print(lst[-1]) 



def get_element():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """

    my_list:list[str] = []
    element:str = input("Please enter an element of the list or press enter. ")
    
    while element != "":
        my_list.append(element)
        element:str = input("Please enter an element of the list or press enter. ")
    return my_list

def main():
    li = get_element()
    get_last_element(li)

if __name__ == "__main__":
    main()