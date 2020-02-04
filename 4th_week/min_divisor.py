def MinDivisor(num):
    if num % 2 == 0:
        return 2
    elif num % 3 == 0:
        return 3
    return int(num)


n = float(input())

print(MinDivisor(n))
