import math

N = int(input())

if N == 1:
    k = 0
else:
    k = math.ceil(math.log2(N))

print(k)