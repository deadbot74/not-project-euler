import math


def abundant(n):
    i = 2
    num = 0
    if math.sqrt(n) - int(math.sqrt(n)) == 0:
        num += int(math.sqrt(n))

    while i < math.sqrt(n):
        if n % i == 0:
            num = num + i + n // i
        i += 1
    num += 1
    if (num > n):
        return True
    else:
        return False


a = []
for i in range(1, 28124):
    if abundant(i):
        a.append(i)

b = []

for k in range(0, 28124):
    b.append(False)

for k in range(0, len(a)):
    for m in range(k, len(a)):
        if a[k] + a[m] <= 28123:
            b[a[k] + a[m]] = True
        else:
            break

sum = 0
for k in range(1, 28123):
    if not b[k]:
        sum += k

print(sum)
