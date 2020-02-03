from math import fabs, sqrt

x, y, xc, yc, r = float(input()), \
                  float(input()), \
                  float(input()), \
                  float(input()), \
                  float(input())


def IsPointInCircle(x, y, xc, yc, r):
    a = fabs(x - xc)
    b = fabs(y - yc)
    c = sqrt(a ** 2 + b ** 2)

    return c <= r


if IsPointInCircle(x, y, xc, yc, r):
    print('YES')
else:
    print('NO')
