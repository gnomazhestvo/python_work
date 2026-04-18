X, Y = map(float, input().split())
coords = list(map(float, input().split()))

A = (coords[0], coords[1])
B = (coords[2], coords[3])
D = (coords[6], coords[7])

Ax, Ay = A

ux = (B[0] - A[0]) / X
uy = (B[1] - A[1]) / X

vx = (D[0] - A[0]) / Y
vy = (D[1] - A[1]) / Y

a11 = 1 - ux
a12 = -vx
a21 = -uy
a22 = 1 - vy

bx = Ax
by = Ay

det = a11 * a22 - a12 * a21

x = (bx * a22 - by * a12) / det
y = (a11 * by - a21 * bx) / det

print(f"{x:.4f} {y:.4f}")