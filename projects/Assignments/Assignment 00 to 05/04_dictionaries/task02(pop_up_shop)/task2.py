def main():
    fruits ={"apple":2,"durain":1.5,"jackfruit":5,"kiwi":1,"rambutan":4,"mango":3}
    total_cost = 0

    for fruit_name in fruits:
        price = fruits[fruit_name]
        amount = int(input("How many (" +fruit_name + ") you want to buy? "))
        total_cost += (price * amount)
        
    print("Your total cost is $"+ str(total_cost) )

if __name__ == "__main__":
    main()