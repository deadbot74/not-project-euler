import itertools
import time

start = time.perf_counter()
a = []
for i in range(1, 10):
    a.append(i)

permuts = list(itertools.permutations(a))
product_sum = []
for i in permuts:
    multiplicand = int(str(i[0]) + str(i[1]))
    multiplier = int(str(i[2]) + str(i[3]) + str(i[4]))
    product = int(str(i[5]) + str(i[6]) + str(i[7]) + str(i[8]))
    if multiplicand * multiplier == product:
        print(multiplicand, multiplier, product)
        if product not in product_sum:
            product_sum.append(product)

    multiplicand = int(str(i[0]))
    multiplier = int(str(i[1]) + str(i[2]) + str(i[3]) + str(i[4]))
    product = int(str(i[5]) + str(i[6]) + str(i[7]) + str(i[8]))
    if multiplicand * multiplier == product:
        print(multiplicand, multiplier, product)
        if product not in product_sum:
            product_sum.append(product)

end = time.perf_counter()
print(end - start)
print(product_sum)
print(sum(product_sum))


