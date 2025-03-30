MAX_LENHT:int = 3

def shorter(lst):
    while len(lst) > MAX_LENHT:
        last=lst.pop()
        print(last)

def get_lst():
    lst:list[str] = []
    elem:str = input("Please enter an element or press enter. ")
    while elem != "":
        lst.append(elem)
        elem:str = input("Please enter an element or press enter. ")
    return lst

def main():
    lst = get_lst()
    shorter(lst)

if __name__ == "__main__":
    main()

    