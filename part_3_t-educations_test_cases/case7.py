n = int(input())
a = list(map(int, input().split()))

vis = [0] * n
cycles = []

def dfs(v):
    path = []
    while not vis[v]:
        vis[v] = 1
        path.append(v)
        v = a[v] - 1
    return path

for i in range(n):
    if not vis[i]:
        cycles.append(dfs(i))

if len(cycles) != 2:
    print(-1, -1)
    exit()

c1, c2 = cycles

x = c1[0]
y = c2[0] + 1

if a[x] == y:
    if len(c2) > 1:
        y = c2[1] + 1
    else:
        print(-1, -1)
        exit()

print(x + 1, y)