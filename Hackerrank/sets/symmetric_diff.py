
m = int(input())
mset = set(map(int, input().split()))
n = int(input())
nset = set(map(int, input().split()))
result = mset.symmetric_difference(nset)
print(result)
