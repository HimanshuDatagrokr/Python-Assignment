# 4. Write a program that can map() to make a list whose elements are squares of numbers
# between 1 and 20 (both included).
# Hints:
# Use map() to generate a list.
# Use Lambda to define anonymous functions.


lambda_sqaure = lambda x : x **2

my_list = []

# adding numbers from 1 to 20
for i in range(1,21):
    my_list.append(i)
  
# squaring the number  
square_number = map(lambda_sqaure, my_list)

# converting map object to list object
squared_number = list(square_number)

print(squared_number)