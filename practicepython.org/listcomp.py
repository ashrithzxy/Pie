'''
Write one line of Python that takes this list a
and makes a new list that has only
the even elements of this list in it.
'''
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [i for i in a if i%2 == 0]
print(b)
'''
WITHOUT LIST COMPREHENSIONS:
a = input().split()
b = []
for i in range(len(a)):
    a[i] = int(a[i])
    if(a[i]%2 == 0):
        b.append(a[i])
print(b)
'''
