a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if ((b <= e and a <= d) or (a <= e and b <= d) or
        (c <= e and a <= d) or (a <= e and c <= d) or
        (b <= e and c <= d) or (c <= e and b <= d)):
    print('YES')
else:
    print('NO')
