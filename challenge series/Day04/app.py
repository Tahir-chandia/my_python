#  Daily Python Challenge – Day 04 Challenge: Convert Numbers to Words
# Todays  task is to write a Python program that converts any given number into words. For example:
import inflect

#  Inflect object create karna
p = inflect.engine()


num = int(input("Enter a number: "))

# To Converts Numbers in to Inwords Numbers
word = p.number_to_words(num).replace(",", "").title() 

print(f"Output: {word}")