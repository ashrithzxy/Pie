'''
Write a program that returns a list that contains only the elements that are common between the lists 
'''
A = input().split()
B = input().split()
C = []
for i in range(len(A)):
    A[i] = int(A[i])
    for j in range(len(B)):
        B[j] = int(B[j])
        if(A[i] == B[j]):
            C.append(A[i])
print(list(set(C)))
