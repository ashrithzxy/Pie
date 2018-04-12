'''
Given a .txt file that has a list of a bunch of names,
count how many of each name there are in the file,
and print out the results to the screen.
'''
with open('nameslist.txt','r') as open_file:
    line = open_file.read().split()
    d_count = 0
    lea_count = 0
    luke_count = 0
    for i in range(len(line)):
        if(line[i] == 'Darth'):
            d_count = d_count+1
        elif(line[i] == 'Lea'):
            lea_count = lea_count+1
        elif(line[i] == 'Luke'):
            luke_count = luke_count+1
    var = list(set(line))
    print(var)
    print(d_count)
    print(lea_count)
    print(luke_count)
