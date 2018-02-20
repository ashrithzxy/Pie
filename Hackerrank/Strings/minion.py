#Vowel consonant game
def game_logic(s):
#KEVIN: VOWELS {A,E,I,O,U}
    vowels = 'AEIOU'
    kevin = 0
    stuart = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevin = kevin + (len(s)-i)
        else:
            stuart = stuart + (len(s)-i)
    if kevin > stuart:
        print("Kevin",kevin)
    elif stuart > kevin:
        print("Stuart",stuart)
    else:
        print("Draw")
s = input()
game_logic(s)
