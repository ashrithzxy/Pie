#percentage marks obtained by a student
n = int(input("Enter the number of records you want to enter: "))
student_marks = {}
for _ in range(n):
    name, *line = input().split() #*line is  extended iterable unpacking, refer: bit.ly/2BYwykW
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input("Enter the student you want to know the percentage of: ")
if query_name in student_marks:
    a = student_marks[query_name]
else:
    print("User not found!")
total = sum(a)
percentage = (total)/3
print('%.2f' %percentage)
