def mutate_string(str, position, character):
    str = str[:int(position)] + character + str[int(position)+1:]
    print(str)
str = input("Enter string:  ")
position, *char = input("Enter position and character:  ").split()
character = char.pop(0)
mutate_string(str, position, character)
