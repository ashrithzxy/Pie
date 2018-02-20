#Write a program to check whether year is leap year or not.
def is_leap(year):
    leap = False
     if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False
    return leap
print("Enter year: ")
year = int(input())
print("Answer: ", is_leap(year))

#def is_leap(year):
#    leap = False
#    if year % 400 == 0:
#        return True
#    if year % 100 == 0:
#        return False
#    if year % 4 == 0:
#        return True
#    return False


#    return leap
