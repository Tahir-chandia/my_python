def get_lst():
    num_lst:list = []
    while True:
        user_input:str = input("Enter a number. ")
        if user_input == "":
            break
        num = int(user_input)
        num_lst.append(num)
    return num_lst
def get_dict(lst):
    num_dict:dict= {}
    for num in lst:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    return num_dict
    
def print_counts(num_dict):
    for num in num_dict:
        print(str(num) + " appears " + str(num_dict[num])+ " times. " )

def main():
    user_numbers = get_lst()
    num_dict = get_dict(user_numbers)
    print_counts(num_dict)

if __name__ == "__main__":
    main()