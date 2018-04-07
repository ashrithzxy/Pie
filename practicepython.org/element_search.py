'''
Write a function that takes an ordered
list of numbers (a list where the
elements are in order from smallest to
largest) and another number.
The function decides whether or not the
given number is inside the list and returns
(then prints) an appropriate boolean.
'''
def binary(my_list,n):
    length = len(my_list)
    mid = length/2
    if(n>mid):
        del my_list[0:mid]
        binary(my_list,n)
    elif(n<mid):
        del my_list[mid:length]
        binary(my_list,n)
    elif(n==mid):
        return True
    else:
        return False
import random
my_list = sorted(random.sample(range(1,50), 15))
n = int(input("Enter the number you want searched: "))
search_result = binary(my_list,n)
print(search_result)
