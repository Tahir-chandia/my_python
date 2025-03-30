def add_many_numbers(numbers)->int:
    """"
    takes a list of numbers and 
    returns the sum of those numbers.
    """
    total:int= 0
    for number in numbers:
        total  += number
    return total

def main():
    numbers:list[int] = [1,2,3,4,5,6]  # Make a list of numbers
    sum_of_numbers:int = add_many_numbers(numbers)  # Find the sum of the list
    print(sum_of_numbers)

if __name__ == "__main__":
    main()