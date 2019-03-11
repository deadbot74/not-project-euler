# Code by Suvankar Sur

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


x = sieve_of_eratosthenes(1000000)


def is_prime(n):
    for i in x:
        if i == n:
            return True
        if i > n:
            return False



max = 0
num1 = num2 = 0

for a in range(-1000, 1001):
    for b in range(-1000, 1001):
        count = 0
        n = 0
        while 1:
            y = n * n + a * n + b
            if is_prime(y):
                n += 1
                count += 1
            else:
                break
        if count > max:
            max = count
            num1 = a
            num2 = b

print(max)
print(num1)
print(num2)
print(num1*num2)
