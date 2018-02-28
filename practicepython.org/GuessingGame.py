import random
rand_number = random.randint(1,9)
number_of_tries = 0
user_input = input("Type 'EXIT' to quit. Enter your guess: ")
while(user_input != "EXIT"):
    user_input = int(user_input)
    if user_input == rand_number:
        print("You guessed it right!!")
    else:
        number_of_tries += 1
        print("Please try again")
        user_input = input("Type 'EXIT' to quit. Enter your guess: ")
