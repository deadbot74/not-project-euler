import sympy


def truncate_front(n):
    front = []
    for i in range(1, len(str(n))):
        front.append(int(str(n)[i:]))
    return front


def truncate_back(n):
    back = []
    for i in range(len(str(n)) - 1, 0, -1):
        back.append(int(str(n)[:i]))
    return back


i = 5
count = 11
total = 0

while count > 0:
    flag = True
    prime = sympy.prime(i)
    if not sympy.isprime(int(str(prime)[0])) or not sympy.isprime(int(str(prime)[-1])):
        i += 1
        continue
    right = prime
    left = 0
    mult = 1
    while right > 0 and flag:
        left += mult * (right % 10)
        flag = sympy.isprime(left) and sympy.isprime(right)
        right //= 10
        mult *= 10
    if flag:
        print(prime)
        count -= 1
        total += prime

    # f = truncate_front(prime)
    # for nums in f:
    #     if not sympy.isprime(nums):
    #         flag = False
    #         break
    # if flag:
    #     b = truncate_back(prime)
    #     for nums in b:
    #         if not sympy.isprime(nums):
    #             flag = False
    #             break
    # else:
    #     i += 1
    #     continue
    i += 1

    del flag, prime

print(total)
