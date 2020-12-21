def recursia(n):
    if n == 0:
        return 0
    elif n == 1:
        return 9
    else:
        return (2 * recursia(n - 1) + 3 * recursia(n - 2))


num = int(input(" введіть значення n:"))
print(recursia(num))