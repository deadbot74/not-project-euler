def is_pand(n):
    num = ""
    is_there = [True]
    for i in range(9):
        is_there.append(False)
    x = 1
    while 1:
        for j in str(n*x):
            if is_there[int(j)]:
                return '0'
            else:
                is_there[int(j)] = True
                num += j
        x += 1
        if len(num) >= 9:
            return num


maximum = 0
num = 0
for i in range(1,9999):
    if int(is_pand(i)) > maximum:
        maximum = int(is_pand(i))
        num = i

print(maximum, num)

