first_max = int(input())
curent_num = int(input())
if curent_num == 0:
    second_max = first_max
else:
    second_max = curent_num

while curent_num != 0:
    if first_max <= curent_num:
        (first_max, second_max) = (curent_num, first_max)
    elif second_max < curent_num:
        second_max = curent_num
    curent_num = int(input())
print(second_max)
