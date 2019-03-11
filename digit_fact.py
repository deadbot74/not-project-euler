import math

sum = 0
for i in range(11, 2540161):
    s = 0
    for j in str(i):
        s += math.factorial(int(j))
        if s > i:
            break
        #   print(s)
    if s == i:
        sum += i

print(sum)
