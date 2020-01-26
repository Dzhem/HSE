a = int(input())
b = int(input())
c = int(input())

i = 0
if a % 2 == 0:
    i += 1
if b % 2 == 0:
    i += 1
if c % 2 == 0:
    i += 1

if i == 1 or i == 2:
    print('YES')
else:
    print('NO')
