import sys
from array import array

l, r, p = map(int, input().split())

if not (1 <= l <= r < p):
    print(0)
    sys.exit()

inv = array('I', [0]) * (r + 1)
inv[1] = 1

for i in range(2, r + 1):
    inv[i] = p - (p // i) * inv[p % i] % p

ans = 0
for x in range(l, r + 1):
    ans += inv[x]
    if ans >= p:
        ans -= p

print(ans)