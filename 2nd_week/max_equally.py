num = int(input())
max_num = num
equal_max = 0

while num != 0:
    if max_num == num:
        equal_max += 1
    if max_num < num:
        max_num = num
        equal_max = 1
    num = int(input())
print(equal_max)
