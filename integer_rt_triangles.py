def find_pythagorean_triplets(n):
    count = 0
    a = 1
    b = a + 1
    c = n - (a + b)
    while a < b and a < n // 3:
        b = a + 1
        while b < c:
            c = n - (a + b)
            if a ** 2 + b ** 2 == c ** 2:
                count += 1
                #   print(a, b, c)
            b += 1
        a += 1
    return count

#   print(find_pythagorean_triplets(840))
max = -1
num = 0
for i in range(6, 1001):
    x = find_pythagorean_triplets(i)
    if x > max:
        max = x
        num = i

print(max, num)
