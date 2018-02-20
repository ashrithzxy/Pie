'''
print function:
input: 3
output: 123
'''
print("Enter n: ")
n = int(input())
print(*range(1,n+1), sep='')
