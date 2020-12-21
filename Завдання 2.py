def perpen(a, b):
    return a[0] * b[0] + a[1] * b[1] == 0

n = int(input('n = '))
a = [[float(input("введіть [{0}][{1}] елемент=".format(i, j))) for j in range(3)] for i in range(n)]
print(a)
b = 0


for i in range(n - 1):
    for j in range(i + 1, n):
        if (perpen(a[i],a[j])):
            b += 1
print(b)