x = int(input())
y = int(input())

day = 1
while x < y:
    x += x * 0.1    # ежедневное увеличение дистанции на 10%
    day += 1
print(day)
