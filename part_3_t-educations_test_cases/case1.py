data = input().split()

A = int(data[0])
B = int(data[1])
C = int(data[2])
D = int(data[3])

variables = [A, B, C, D]

for variable in variables:
    if variable >= 1 and variable <= 100:
        if D > B:
            sum = A + C*(D-B)
        else:
            sum = A
    else:
        sum = 'error'
        break

print(sum)