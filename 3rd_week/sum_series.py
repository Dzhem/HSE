n = int(input())
i = 1
sum_series = 0

while i <= n:
    sum_series += 1 / i ** 2
    i += 1

print(sum_series)
