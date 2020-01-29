from math import floor, ceil

num = float(input())
num_rus_round = 0

if num % 1 < 0.5:
    num_rus_round = floor(num)
else:
    num_rus_round = ceil(num)

print(num_rus_round)
