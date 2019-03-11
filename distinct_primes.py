from sympy import factorint
import time

start = time.perf_counter()

i = 2 * 3 * 5 * 7

while 1:
    if len(factorint(i)) >= 4 and len(factorint(i + 1)) >= 4 and len(factorint(i + 2)) >= 4 and len(
            factorint(i + 3)) >= 4:
        print(i)
        break
    else:
        i += 1
end = time.perf_counter()
print(end - start)
