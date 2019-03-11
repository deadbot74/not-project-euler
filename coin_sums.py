import itertools

coins = [1, 2, 5, 10]
sum_total = 20
combinations_list = []
for i in range(1, len(coins) + 1):
    combinations_list.append(list(itertools.combinations(coins, i)))

print(combinations_list)
count = 0
for i in range(len(combinations_list)):
    for j in range(len(combinations_list[i])):
        l = 1
        n = 1
        while l < len(combinations_list[i][j]):
            temp = sum_total

            for k in range(len(combinations_list[i][j]) -1, -1, -1):
                if temp <= 0:
                    l += 1
                    n = 2
                    break
                elif k == 0:
                    if temp % combinations_list[i][j][k] == 0:
                        count += 1
                        n += 1
                        break
                elif k == l:
                    temp -= n*combinations_list[i][j][k]
                else:
                    temp -= combinations_list[i][j][k]


print(count)



