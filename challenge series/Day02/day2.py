# Day 2- Python Challange:
## Task-1 :

# "Write a Python Program where user can  write words or sentences show the output to count the words or sentences"

#Task 2:

# "Write the same program but the answere should be reversed"

user=input("Enter Yours Words or Sentences to count")
user_split=user.split()
user_count = len(user_split)
print(user_count)
reversed_words = " ".join(reversed(user_split))
print(reversed_words)
