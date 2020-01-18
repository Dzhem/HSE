x_cell1 = int(input())
y_cell1 = int(input())
x_cell2 = int(input())
y_cell2 = int(input())
answer = 'NO'

if (x_cell2 - x_cell1) % 2 == 0:
    if (y_cell2 - y_cell1) % 2 == 0:
        answer = 'YES'
if (x_cell2 - x_cell1) % 2 == 1:
    if (y_cell2 - y_cell1) % 2 == 1:
        answer = 'YES'
print(answer)
