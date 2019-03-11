sum = 0
for i in range(1001):
    if i % 10 == 0:
        sum += 0
    else:
        sum += i ** i % 10 ** 10

print(sum % 10 ** 10)
