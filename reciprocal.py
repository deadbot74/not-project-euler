

"""x = 1 / 3
print(x)
print((x * 10) % 3)
print(x * 10 - int(x * 10))
print(x - ((x * 10 - int(x * 10))))
y = (x * 10 - int(x * 10))
if(y>1e-10):
    print('Yes')


import math

t = int(input())
for k in range(0, t):
    n = int(input())
    x = 2 ** n
    sum = 0
    while x > 0:
        r = x % 10
        x = x // 10
        sum += r
    print(sum)




maxn = -1
num = 0
for i in range(length - 1, -1, -1):
    for k in range(i - 1, -1, -1):
        v = x[i]
        j = k
        m = 0
        while v > 0:
            v -= x[j]
            j -= 1
            m += 1
        if v == 0 and maxn < m:
            maxn = m
            num = x[i]

print(num)
"""


def prime_factorisation(n):
    i = 2
    a = []
    count = 0
    while n > 0 and i <= n:
        if n == i:
            a.append(i ** (count+1))
            break

        if n % i == 0:
            n = n / i
            count += 1
        else:
            if count == 0:
                i += 1
            else:
                a.append(i ** count)
                count = 0
                i += 1

    return a


x = prime_factorisation(194)
a=[1,2,3,4]
set1 = {1,2,3}
set2 = {3,2,5}
#print(set1.intersection(set2))
#print(set(a))
#print(len(set1))
b=a[:]
for i in range(0, len(b)):
    b[i]+=2
  #  print(i)

print(a,b)
