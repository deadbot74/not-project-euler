import sympy

def prime_factorisation(n):
    return sympy.factorint(n)


prime_dict = prime_factorisation(160)
# print(prime_dict)

maximum = 0
number = 0
i = 1000000
ratio = 1
while i >= 10:
    if sympy.isprime(i):
        i -= 1
        continue
    totient_value = 1
    prime_dict = prime_factorisation(i)
    for key, value in prime_dict.items():
        if value == 1:
            totient_value *= key - 1
        else:
            totient_value *= key ** value - key ** (value - 1)
    ratio = i/totient_value
    if ratio > maximum:
        maximum = ratio
        number = i
    i -= 1

print(maximum, number)



