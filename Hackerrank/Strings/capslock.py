#Capitalize first and last name
def capslock(names):
    for i in range(len(names)):
        string = names[i]
        if(names[i].isalpha() == True):
            string = string.title();
            names[i] = string
    final = ' '.join(names)
    return final
names = input().split(' ')
capital = capslock(names)
print(capital)


#q w e r t y u i o p a s d f g h j  k l z x c v b n m Q W E R T Y U I O P A S D F G H J  K L Z X C V B N M
#1 2 2 3 4 5 6 7 8  9
