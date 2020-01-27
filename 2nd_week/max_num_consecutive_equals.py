prev_num = int(input())
cur_num = int(input())
max_num_cons_eq = 1
cur_max_num_cons_eq = 1

while cur_num != 0:
    if prev_num == cur_num:
        cur_max_num_cons_eq += 1
    elif max_num_cons_eq < cur_max_num_cons_eq:
        max_num_cons_eq = cur_max_num_cons_eq
        cur_max_num_cons_eq = 1
    prev_num = cur_num
    cur_num = int(input())
if max_num_cons_eq < cur_max_num_cons_eq:
    max_num_cons_eq = cur_max_num_cons_eq
print(max_num_cons_eq)
