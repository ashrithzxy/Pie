num_elements = int(input())
myset = set(map(int, input().split()))
#num_commands =  int(input())
for i in range(int(input())):
    comm = input().split()
    for j in range(1,len(comm)):
        comm[j] = int(comm[j])

    if comm[0] == "pop":
        myset.pop()
    elif comm[0] == "remove":
        myset.remove(comm[j])
    elif comm[0] == "discard":
        myset.discard(comm[j])
        
print(sum(myset))
