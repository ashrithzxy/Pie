print("Enter a number: ")
n = int(input())
if (n%2==0 and 2<=n<=5):
    print("Even25")
elif(n%2==0 and 6<=n<=20):
    print("Even620")
elif (n%2==0 and n>20):
    print("Even20up")
elif(n%2==1):
    print("ODD")
