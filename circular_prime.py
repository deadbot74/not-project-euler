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


def generate_circular_perms(nums: list):
    perms = []
    for i in range(len(nums)):
        x = []
        for j in range(i, len(nums)):
            x.append(nums[j])
        for j in range(0, i):
            x.append(nums[j])
        perms.append(x)
        del x
    return perms


prime_dict = sieve_of_eratosthenes(1000000)
number_count = 0

# print(prime_dict.keys())

for i in prime_dict.keys():
    num_list = []
    for j in str(i):
        num_list.append(int(j))
    permutations = generate_circular_perms(num_list)
    flag = True
    for j in permutations:
        integer_st = ""
        for k in range(len(j)):
            integer_st += str(j[k])
        if not prime_dict.get(int(integer_st), False):
            flag = False
            break
    if flag:
        print(i)
        number_count += 1


print(number_count)
