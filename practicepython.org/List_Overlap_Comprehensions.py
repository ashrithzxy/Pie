'''
write a program that
returns a list that contains only the
elements that are common between the lists
'''

'''
Without list comprehensions

l1 = input().split()
l2 = input().split()
l3 = []
for i in range(len(l1)):
    l1[i] = int(l1[i])
    for j in range(len(l2)):
        l2[j] = int(l2[j])
        if (l1[i] == l2[j]):
            l3.append(l1[i])
print(l3)
'''
'''
With list comprehensions
'''
l1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]#input().split()
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]#input().split()
l3 = [i for i in l1 if i in l2]
print(l3)
