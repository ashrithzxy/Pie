'''
Given an integer, n, and n space-separated integers as input, create a tuple, t, of those n integers. Then compute and print the result of hash(t).
'''
n = input()
print (hash(tuple([int(i) for i in input().split()])))
