n, k = map(int, input().split())
a = input().split()

freq = {}

for num in a:
    length = len(num)
    for i, ch in enumerate(num):
        d = ord(ch) - 48
        place = 10 ** (length - i - 1)
        gain = (9 - d) * place

        freq[gain] = freq.get(gain, 0) + 1
        
ans = 0
taken = 0

for gain in sorted(freq.keys(), reverse=True):
    cnt = freq[gain]
    use = min(cnt, k - taken)
    ans += use * gain
    taken += use
    if taken == k:
        break

print(ans)