'''
Given two .txt files that have lists of numbers in them,
find the numbers that are overlapping. 
One .txt file has a list of all prime numbers under 1000,
and the other .txt file has a list of happy numbers up to 1000.
'''overlapp = []
with open('primenumbers.txt', 'r') as primefile:
    prime_numbers = primefile.read().split()
    for i in range(len(prime_numbers)-1):
        prime_numbers[i] = int(prime_numbers[i])
    with open('happynumbers.txt', 'r') as happyfile:
        happy_numbers = happyfile.read().split()
        for j in range(len(happy_numbers)-1):
            happy_numbers[j] = int(happy_numbers[j])
        #print(prime_numbers)
        #print(happy_numbers)
        for k in range(len(prime_numbers)-1):
            for j in range(len(happy_numbers)-1):
                if(prime_numbers[k] == happy_numbers[j]):
                    overlapp = overlapp.append(prime_numbers[i])
    print(overlapp)
