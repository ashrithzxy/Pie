'''
Write a program that
asks the user how many Fibonnaci numbers
to generate and then generates them.
'''
def fibo(n):
    first = 0
    second = 1
    count = 2
    #print(first)
    print(second)
    while(count<=n):
        next = first + second
        print(next)
        count += 1
        first = second
        second = next
n = int(input("Enter the number of digits you want to generate: "))
fibo(n)
