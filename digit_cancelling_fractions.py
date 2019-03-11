l = "123"

k = "234"

print(k.index(l[1]))

for i in range(10, 99):
    for j in range(i+1,100):
        fract = i / j
        for k in range(0,len(str(i))):

            if str(i)[k] in str(j):
                index = str(j).index(str(i)[k])
                if k == 0:
                    i %= 10
                else:
                    i //= 10
                if index == 0:
                    j %= 10
                else:
                    j //= 10
                x = i / j
                if x == fract:
                    print(i,j)

                break

