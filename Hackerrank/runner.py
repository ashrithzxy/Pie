n = int(input())
rank = []
for i in range(n):
    s = int(input())
    rank.append(s)
rank.sort()
print("sorted list is: ", rank)
print("second largest element is: ", rank[n-2])
