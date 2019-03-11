import itertools
import time

nums = [0,1,2,3,4,5,6,7,8,9]
start = time.perf_counter()
x = list(set(itertools.permutations(nums)))

x.sort()
end = time.perf_counter()
print(start, end, end - start)
print(x[999999])
