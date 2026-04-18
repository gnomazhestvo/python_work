n = int(input())
a = list(map(int, input().split()))

bad_odd = []
bad_even = []

for i in range(n):
    if (i + 1) % 2 != a[i] % 2:
        if (i + 1) % 2 == 1:
            bad_odd.append(i)
        else:
            bad_even.append(i)

if len(bad_odd) == 0 and len(bad_even) == 0:
    print(-1, -1)

elif len(bad_odd) == 1 and len(bad_even) == 1:
    print(bad_odd[0] + 1, bad_even[0] + 1)

else:
    print(-1, -1)