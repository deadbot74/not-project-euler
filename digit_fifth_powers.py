import math

sum = 0
for i in range(11, 354295):
    s = 0
    for j in str(i):
        s += int(j)**5
        if s > i:
            break
    if s == i:
        print(i)
        sum += i

print(sum)
