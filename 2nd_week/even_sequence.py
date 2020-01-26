even_seq = 0
num = int(input())
while num != 0:
    if num % 2 == 0:
        even_seq += 1
    num = int(input())
print('\n', even_seq, end='', sep='')
