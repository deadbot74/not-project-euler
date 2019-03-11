import math


def is_hexa(x):
    n = (math.sqrt(8 * x + 1) + 1) / 4
    if n - int(n) == 0:
        return True
    else:
        return False


def is_penta(x):
    n = (math.sqrt(24 * x + 1) + 1) / 6
    if n - int(n) == 0:
        return True
    else:
        return False


# def is_triangular(x):
#     n = (math.sqrt(8 * x + 1) - 1) / 2
#     if n - int(n) == 0:
#         return int(n)
#     else:
#         return 0


i = 144

while 1:
    n = i * (2*i - 1)
    if is_penta(n):
        print(n)
        break
    i += 1



