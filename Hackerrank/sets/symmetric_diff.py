m = int(input())
mset = set(map(int, input().split()))
n = int(input())
nset = set(map(int, input().split()))
result = mset.symmetric_difference(nset)
print(result)

#-----------for printing on different lines
#m = int(input())
#mset = set(map(int, input().split()))
#n = int(input())
#nset = set(map(int, input().split()))
#result = list(mset.union(nset) - mset.intersection(nset))
#result.sort()
#for i in range(len(result)):
#    print(result[i])
