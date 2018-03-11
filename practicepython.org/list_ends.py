'''
Write a program that takes a list of numbers
and makes a new list of only
the first and last elements of the given list.
'''
import random
def list_ends(my_list):
    final_list = []
    final_list.append(my_list[0])
    final_list.append(my_list[len(my_list)-1])
    print("First and Last elements of the list are ",final_list, " respectively.")
my_list = random.sample(range(10), 5)
print("List is: ",my_list)
list_ends(my_list)
