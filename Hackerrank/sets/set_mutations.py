num_elements = int(input())
A = set(map(int, input().split()))
num_sets = int(input())
for i in range(num_sets):
    command = input().split()
    opset = set(map(int, input().split()))
    for j in range(1, len(command)):
        command[j] = int(command[j])

    if command[0] == "intersection_update":
        A.intersection_update(opset)
    elif command[0] == "update":
        A.update(opset)
    elif command[0] == "symmetric_difference_update":
        A.symmetric_difference_update(opset)
    elif command[0] == "difference_update":
            A.difference_update(opset)
print(sum(A))
