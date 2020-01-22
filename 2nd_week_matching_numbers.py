n1 = int(input())
n2 = int(input())
n3 = int(input())

i = 0
if n1 == n2 == n3:
    i = 3
elif n1 == n2 or n2 == n3 or n1 == n3:
    i = 2
print(i)
