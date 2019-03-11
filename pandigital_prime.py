import itertools
import math


def sieve_of_eratosthenes(n):
    a = []
    for index in range(0, n + 1):
        a.append(True)

    for index in range(2, int(math.sqrt(n)) + 1):
        j = index * index
        while j <= n:
            a[j] = False
            j = j + index

    b = {}
    for index in range(2, n + 1):
        if a[index]:
            b[index] = True

    return b


ints = [1, 2, 3, 4, 5, 6, 7]

prime_dict = sieve_of_eratosthenes(7654321)
num = 0
maximum = 0
for i in range(len(ints) - 1):
    perms = list(itertools.permutations(ints))
    perms.sort()
    perms.reverse()
    flag = False
    for j in perms:
        integer_st = ""
        for k in range(len(j)):
            integer_st += str(j[k])
        if prime_dict.get(int(integer_st), False):
            num = int(integer_st)
            flag = True
            break
    if flag and num > maximum:
        print(num)
        break
    del perms
    ints.pop()

print(maximum)


