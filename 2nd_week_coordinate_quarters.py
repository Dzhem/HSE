x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())

quart_x = 0
quart_y = 0

if x1 > 0:
    if x2 > 0:
        quart_x = 1
    else:
        quart_x = 2
elif x1 < 0:
    if x2 < 0:
        quart_x = 3
    else:
        quart_x = 4

if y1 > 0:
    if y2 > 0:
        quart_y = 1
    else:
        quart_y = 2
elif y1 < 0:
    if y2 < 0:
        quart_y = 3
    else:
        quart_y = 4

if quart_x == quart_y:
    print('YES')
else:
    print('NO')
