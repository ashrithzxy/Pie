def avg(array):
    total = sum(set(array))
    average = total/len(set(array))
    print(average)
n = int(input())
arr = list(map(int, input().split()))
avg(arr)
