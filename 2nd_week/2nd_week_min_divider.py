n = int(input())

i = n
while i > 1:
    if n % i == 0:
        min_div = i
    i -= 1
print(min_div)
