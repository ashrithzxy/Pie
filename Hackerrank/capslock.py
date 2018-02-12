def capslock(names):
    for i in range(len(names)):
        string = names[i]
        if(names[i].isalpha() == True):
            string = string.title();
            names[i] = string
    final = ' '.join(names)
    return final
names = input().split()
capital = capslock(names)
print(capital)
