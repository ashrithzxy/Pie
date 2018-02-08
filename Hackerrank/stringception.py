def substring(str1, substr):
    count = 0
    for i in range(len(str1) - len(substr) + 1):
        if str1[i:i+len(substr)] == substr:
            count += 1
    print(count)
str1 = input()
substr = input()
substring(str1, substr)
