n, t = map(int, input().split())
a = list(map(int, input().split()))
k = int(input()) - 1
a.sort()

L = a[0]
R = a[-1]
f = a[k]

base = R - L
can_reach = (f - L <= t) or (R - f <= t)

if can_reach:
    ans = base
else:
    ans = base + min(abs(f - L), abs(f - R))

print(ans)