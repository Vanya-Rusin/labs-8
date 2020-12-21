import math


def f(x, ):
    if x < 0:
        g = 1 + x / math.factorial(2) + x ** 2 / math.factorial(3) + x ** 8 / math.factorial(9)
        return g
    elif 0 <= x <= 5:
        v = 15 + math.sqrt(math.cos(x ** 6))
        return v
    elif x > 5:
        k = min(1,2 * math.sin(x))
        return k


a = float(input('a='))
b = float(input('b='))
print("max{f(a),f(b)}", f(max(f(a), f(b))))
print('f(3)', f(3))
m = f(max(f(a), f(b))) - f(3)
print(m)



#a = []
#n = 0
#x = int(input('введіть значення х:'))
#for i in range(1,x+2):
#    a.append(1+x**n/math.factorial(n+1))
#    n += 1
#print(a)
#g = sum(a)
#print(g)