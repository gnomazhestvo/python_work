import sys

n = int(input())
poly = [tuple(map(float, input().split())) for _ in range(n)]


def total_area():
    s = 0
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]
        s += x1 * y2 - x2 * y1
    return abs(s) / 2


S = total_area()
target = S / 2


def left_area(mid):
    clipped = []

    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]

        # полностью слева
        if x1 <= mid and x2 <= mid:
            clipped.append((x2, y2))

        # слева -> справа
        elif x1 <= mid and x2 > mid:
            if x2 != x1:
                t = (mid - x1) / (x2 - x1)
                yi = y1 + t * (y2 - y1)
                clipped.append((mid, yi))

        # справа -> слева
        elif x1 > mid and x2 <= mid:
            if x2 != x1:
                t = (mid - x2) / (x1 - x2)
                yi = y2 + t * (y1 - y2)
                clipped.append((mid, yi))
                clipped.append((x2, y2))

    # считаем шнуровку по корректному контуру
    if len(clipped) < 3:
        return 0.0

    s = 0
    for i in range(len(clipped)):
        x1, y1 = clipped[i]
        x2, y2 = clipped[(i + 1) % len(clipped)]
        s += x1 * y2 - x2 * y1

    return abs(s) / 2


lo = min(x for x, y in poly)
hi = max(x for x, y in poly)

for _ in range(70):
    mid = (lo + hi) / 2
    if left_area(mid) < target:
        lo = mid
    else:
        hi = mid

print(f"{(lo + hi) / 2:.10f}")