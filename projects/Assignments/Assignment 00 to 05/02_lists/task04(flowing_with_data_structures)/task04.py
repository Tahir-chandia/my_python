def add_three_copies(message_list,data):
    for i in range(3):#Loop in 3 times
        message_list.append(data) # add data in message list

def main():
    mylist:list[str] = [] # first my list is is empty
    message:str = input("Enter message to make copies: ") 
    print("List before: ",mylist) 
    add_three_copies(mylist,message) # add the message in data
    print("List after: ",mylist)

if __name__ == "__main__":
    main()
