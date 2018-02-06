n = int(input())

rank = []
#for i in range(int(input())):
rank = map(int, n.split())
    #for i in range(len(rank)):
    #    rank[i] = int(rank[i])
rank.sort()
print("sorted list is: ", rank)
print("second largest element is: ", rank[n-2])


#rank = []
#diff = []
#for i in range(n):
#    s = int(input())
#    rank.append(s)
#rank.sort()
#print("sorted list is: ", rank)
#for i in range(len(rank)-1):
#    if(rank[i] == rank[i+1]):
#        rank.remove(rank[i])
#print(rank)
#n = len(rank)
#print("second largest element is: ", rank[n-2])













#for i in range(len(rank)-1):
#    if(rank[i]<=rank[i+1]):
#        largest = rank[i+1]
#for i in range(len(rank)):
#    diff.append(largest - rank[i])
#print(diff)
