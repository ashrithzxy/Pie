num_english = int(input())
english = set(map(int, input().split()))
num_french = int(input())
french = set(map(int, input().split()))
total = len(french.union(english))
print(total)