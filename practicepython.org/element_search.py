'''
Write a function that takes an ordered
list of numbers (a list where the
elements are in order from smallest to
largest) and another number.
The function decides whether or not the
given number is inside the list and returns
(then prints) an appropriate boolean.
'''
def binary(my_list):

import random
my_list = sorted(random.sample(range(1,50), 15))
n = input("Enter the number you want searched: ")
search_result = binary(my_list)
print(search_result)
