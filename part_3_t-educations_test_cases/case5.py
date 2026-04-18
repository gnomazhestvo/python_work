l, r = map(int, input().split())

count = 0

for digit in range(1, 10):
    num = 0
    for length in range(1, 19):
        num = num * 10 + digit
        if num > r:
            break
        if num >= l:
            count += 1

print(count)