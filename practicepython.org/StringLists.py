'''
Find whether string is pallindrome or not
'''
s = input("Enter word: ")
x = ''
for i in range(len(s)):
    x += s[len(s)-1-i]
if(x==s):
    print("Pallindrome")
else:
    print("not pallindrome")
