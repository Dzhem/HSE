cur_num = int(input())
max_num = cur_num
while cur_num != 0:
    if cur_num != 0 and max_num < cur_num:
        max_num = cur_num
    cur_num = int(input())
print(max_num)
