A = set(map(int, input().split()))
result = 0
num = int(input())
for i in range(num):
    n = set(map(int, input().split()))
    if(A.issuperset(n)):
        result += 1
    else:
        result = 0
if (result == num):
    print("True")
else:
    print("False")
