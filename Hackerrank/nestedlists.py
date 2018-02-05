print("Enter the number of student records: ")
n = int(input())
report = []
print("Enter student details: ")
for outer in range(n):
    data = []
    for inner in range(2):
        s = input()
        data.append(s)
        lens = len(data)
        for x in range(1,lens):
            data[x] = float(data[x])
    report.append(data)
print("Nested List is: ", report)
