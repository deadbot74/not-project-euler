# Code By Suvankar Sur

import math


def sieve_of_eratosthenes(n):
    a = []
    for i in range(0, n + 1):
        a.append(True)

    for i in range(2, int(math.sqrt(n)) + 1):
        j = i * i
        while j <= n:
            a[j] = False
            j = j + i

    b = []
    for i in range(2, n + 1):
        if a[i]:
            b.append(i)

    return b


x = sieve_of_eratosthenes(100000)
# print(x)
y = []

for i in range(3, 100000):
    if i % 2 != 0:
        y.append(i)

z = list(set(y) - set(x))
# print(z)

n = 0
for i in z:
    for j in x:
        for k in range(1, 100000):
            if j < i and i > 2 * k * k:
                n = j + 2 * k * k
                if n > i:
                    break
                if n == i:
                    break
            else:
                break
        if n == i:
            break
    if n != i:
        print(i)
        break
