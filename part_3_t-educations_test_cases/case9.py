import sys

n = int(input())

if n == 0:
    print(0)
    exit()

a = [int(input()) for _ in range(n)]

INF = 10**18
dp = [INF] * (n + 1)
dp[0] = 0

for cost in a:
    new_dp = [INF] * (n + 1)

    for coupons in range(n + 1):
        if dp[coupons] == INF:
            continue

        nc = coupons + (1 if cost > 100 else 0)
        
        if nc <= n:
            new_dp[nc] = min(new_dp[nc], dp[coupons] + cost)

        if coupons > 0:
            new_dp[coupons - 1] = min(new_dp[coupons - 1], dp[coupons])

    dp = new_dp

print(min(dp))