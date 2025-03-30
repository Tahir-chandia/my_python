def read_phone_numbers():
    """
    Ask the user for names/numbers to story in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook:dict = {} 
    
    while True:
        name:str = input("Name: ")
        if name == "":
            break
        number:int =int(input("Number: "))
        phonebook[name] = number
    return phonebook

def print_numbers(phonebook):
    """
    Prints out all the names/numbers in the phonebook.
    """
    for name in phonebook:
        print(str(name)+" -> "+ str(phonebook[name]))

def lookup_numbers(phonebook):
    """
    Allow the user to lookup phone numbers in the phonebook
    by looking up the number associated with a name.
    """
    while True:
        name:str = input("Enter name to lookup ")
        if name =="":
            break
        if name not in phonebook:
            print(name+"not in phoonebook")
        else:
            print(phonebook[name])

def main():
    phonebook = read_phone_numbers()
    print_numbers(phonebook)
    lookup_numbers(phonebook)

if __name__ == "__main__":
    main()
      