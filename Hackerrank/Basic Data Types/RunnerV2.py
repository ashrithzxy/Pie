#Find Runner up score

#print("Enter the number of elements you want in the list: ")
#n = int(input())
print("Enter the elements of the list: ")
#for i in range(n):
rank = list(map(int, input().split()))
rank.sort()
rank = list(set(rank))
print(rank)
m = len(rank)
print("Second largest element is: ", rank[m-2])
