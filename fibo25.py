# Code by Suvankar Sur

def no_of_terms(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count


a = 1
b = 1
x = 2
while 1:
    c = a + b
    a = b
    b = c
    x += 1
    if no_of_terms(c) == 1000:
        print(x)
        print(c)
        break
