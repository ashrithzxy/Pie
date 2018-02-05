print("Enter the number of student records: ")
n = int(input())
report = []
print("Enter student details: ")
for outer in range(n):
    data = []
    for inner in range(2):
        s = input()
        data.append(s)
        lens = len(data) #length of list "data"
        for x in range(1,lens):
            data[x] = float(data[x])
    report.append(data)
print("Nested List is: ", report) #code till here creates nested the nested list
s = sorted(set([x[1] for x in report]))
for name in sorted(x[0] for x in report if x[1] == s[1]):
    print(name) 
