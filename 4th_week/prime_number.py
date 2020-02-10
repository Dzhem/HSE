def MinDivisor(n):
    i = 2
    while n % i != 0:
        if i >= n ** 0.5:
            return int(n)
        i += 1
    return int(i)


def IsPrime(num):
    return num == MinDivisor(num)


n = float(input())

if IsPrime(n):
    print('YES')
else:
    print('NO')
