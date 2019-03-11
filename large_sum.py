f = open("E:\Python\p013_largesum.txt")
numbers = f.read().split("\n")
sum = 0
print(numbers)
for number in numbers:
    sum += int(number)

print(sum//10**40)