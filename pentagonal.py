import math


def is_pentagonal(x):
    n = (math.sqrt(24*x+1)+1)/6
    if n - int(n) == 0:
        return True
    else:
        return False


def penta(n):
    return n*(3*n-1)//2

pentagonal = []

for i in range(1,25000):
    pentagonal.append(penta(i))

print(pentagonal)
minimum = 0xfffffff
d = minimum
for i in range(2,len(pentagonal)):
    j = i-1
    if pentagonal[i] - pentagonal[j] > d:
        break
    while j >= 0:
        if pentagonal[i] - pentagonal[j] > d:
            break
        if is_pentagonal(pentagonal[i] - pentagonal[j]) and is_pentagonal(pentagonal[i] + pentagonal[j]):
            d = pentagonal[i] - pentagonal[j]
        if d < minimum:
            minimum = d
        j -= 1

print(minimum)