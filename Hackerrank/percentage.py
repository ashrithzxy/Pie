print("Enter the number of student records: ")
n = int(input())
report = []
print("Enter student details: ")
for outer in range(n):
    data = []
    for inner in range(3):
        s = input()
        data.append(s)
        lens = len(data)
    #print(lens)     #length of list "data"
        for x in range(1,lens):
            data[x] = float(data[x])
    report.append(data)
print(report)
#lol = dict(report) #ValueError: dictionary update sequence element #0 has length 4; 2 is required
#print(lol)
