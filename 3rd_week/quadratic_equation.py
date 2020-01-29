from math import fabs
a = float(input())
b = float(input())
c = float(input())
eps = 5 * 10 ** -6

d = b ** 2 - (4 * a * c)
if d + eps >= 0:
    x1 = (-b - d ** (1 / 2)) / (2 * a)
    x2 = (-b + d ** (1 / 2)) / (2 * a)
    if fabs(x1 - x2) < eps:
        print(x1)
    elif x1 + eps < x2:
        print(x1, x2)
    else:
        print(x2, x1)
