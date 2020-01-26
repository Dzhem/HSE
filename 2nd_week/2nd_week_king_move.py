x_king = int(input())
y_king = int(input())
x_move = int(input())
y_move = int(input())
answer = 'NO'

if -1 <= x_move - x_king <= 1:
    if -1 <= y_move - y_king <= 1:
        answer = 'YES'
if x_move == x_king:
    if y_move == y_king:
        answer = 'NO'
print(answer)
