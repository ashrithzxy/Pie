'''
Write a program (using functions!) that asks the user
for a long string containing multiple words.
Print back to the user the same string,
except with the words in backwards order. 
'''
def reverse(inp):
    return ' '.join(inp.split()[: : -1])
inp = input("Enter your string: ")
r = reverse(inp)
print(r)
