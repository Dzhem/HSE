x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if y2 > y1 and (x1 - (y2 - y1) <= x2 <= x1 + (y2 - y1)):
    if (y2 % 2 == 0 and x2 % 2 == 0) or (y2 % 2 != 0 and x2 % 2 != 0):
        print('YES')
    else:
        print('NO')
else:
    print('NO')
