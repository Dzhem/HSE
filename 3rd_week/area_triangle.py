a = float(input())
b = float(input())
c = float(input())

p = 1 / 2 * (a + b + c)
s = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)

print(s)
