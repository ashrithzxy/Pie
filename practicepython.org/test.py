def prime_check(number):
    prime = True
    if number == 1:
        prime = False
    elif number == 2:
        prime = True
    else:
        prime = True
        for i in range(2, number+1):
            if(number%i == 0):
                prime = False
                break
    return prime
number = int(input("Enter the number you want to check primality for: "))
is_prime = prime_check(number)
print(is_prime)
