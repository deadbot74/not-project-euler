import itertools
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
    return a


d = {
    1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"
}
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = list(itertools.permutations(nums, 4))

integers = []

for i in x:
    s = ""
    for j in i:
        s += d[j]
    integers.append(int(s))

for i in integers:
    if i % 2 == 0:
        integers.remove(i)

primes = sieve_of_eratosthenes(10000)
dt = 1665
index = integers.index(1487)
print(index)
print(integers[index] + 2*dt)
print(integers.index(4817))
print(primes[integers[index] + 4*dt])

while index + 4 * dt < len(integers):
    if primes[integers[index]] and primes[integers[index] + 2 * dt] and primes[integers[index] + 4 * dt]:
        print("hello")
        break
    dt += 5
