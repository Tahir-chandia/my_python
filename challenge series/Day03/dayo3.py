
# Day 03- Python Challange:
# 🚀 Challenge: Write a Python Program which take a number and check that number is it Prime number or not!🔢💡

num:int =int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")