a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())

v1 = a1 * b1 * c1
v2 = a2 * b2 * c2

min_side1 = a1
if min_side1 > b1:
    min_side1 = b1
if min_side1 > c1:
    min_side1 = c1

min_side2 = a2
if min_side2 > b2:
    min_side2 = b2
if min_side2 > c2:
    min_side2 = c2

if min_side2 > min_side1:
    print(0)
else:
    print(v1 // v2)
