'''
Write a program that prints out all the elements of the list that are less than 5.
'''
mylist = input("Enter list elements: ").split()
n = int(input("Enter number you want to compare with: "))
newlist = []
for i in range(len(mylist)):
    mylist[i] = int(mylist[i])
    if(mylist[i] < n):
        newlist.append(mylist[i])
        print(newlist[i], end=' ')
#EXTRA
#mylist = input().split();
#print([(mylist[i]) for i in range(len(mylist)) if(int(mylist[i])<10)])
