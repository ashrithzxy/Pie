'''
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
'''
import datetime
name = input("Enter your name: ")
age = int(input("Enter your age: "))
current_year = datetime.datetime.now().year
century = (current_year-age)+100
print("Hey {}, you'll be 100 years old in {}".format(name,century))
#EXTRAS
#for i in (range(int(input()))):
    #print("Hey {}, you'll be 100 years old in {}".format(name,century), end='')
    #print("Hey {}, you'll be 100 years old in {}".format(name,century))
