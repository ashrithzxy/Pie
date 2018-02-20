a = int(input("Enter a: "))
print("{} is even.".format(a)) if(a%2 == 0) else print("{} is odd.".format(a))
#EXTRAS:
print("{} is a multiple of 4.".format(a)) if(a%4 == 0) else print("{} is not a multiple of 4.".format(a))
b = int(input("Enter b: "))
print("{} divides evenly by {}.".format(a,b)) if(a%b == 0) else print("{} does not divide evenly by {}.".format(a,b))
