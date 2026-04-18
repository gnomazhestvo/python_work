import heapq

N = int(input())
A, B, C = map(int, input().split())

a, b, c = sorted([A, B, C])

INF = 10**30
dist = [INF] * a
dist[0] = 0

pq = [(0, 0)]

while pq:
    d, r = heapq.heappop(pq)
    if d > dist[r]:
        continue

    for coin in (b, c):
        nr = (r + coin) % a
        nd = d + coin
        if nd < dist[nr]:
            dist[nr] = nd
            heapq.heappush(pq, (nd, nr))

limit = N - 1
ans = 0

for r in range(a):
    if dist[r] <= limit:
        ans += (limit - dist[r]) // a + 1

print(ans)