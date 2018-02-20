'''
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
'''
number = int(input("Enter number: "))
mylist = []
for i in range(1, number+1):
    if(number%i == 0):
        mylist.append(i)
print(mylist)
