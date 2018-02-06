print("Enter the number of student records: ")
n = int(input())
report = []
print("Enter student details: ")
for outer in range(n):
    data = []
    for inner in range(4):
        s = input()
        data.append(s)
        lens = len(data)
    #print(lens)     #length of list "data"
        for x in range(1,lens):
            data[x] = float(data[x])
    report.append(data)
for o in report:
    marks = tuple()
    for p in (o[1:]):
        marks += (p,)
    temp = []
    temp.append(o[0])
    temp.append(marks)
    report = temp
print(report)
total = sum(marks)
percentage = total/3
print('%.2f' %percentage)
#card = dict(report) #ValueError: dictionary update sequence element #0 has length 4; 2 is required
#print(card)
