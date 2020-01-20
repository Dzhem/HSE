apart1 = int(input())
apart2 = int(input())

if (apart1 - 1) % (apart2 - apart1 + 1) == 0:
    print('YES')
else:
    print('NO')
