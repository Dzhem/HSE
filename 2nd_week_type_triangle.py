a = int(input())
b = int(input())
c = int(input())

if a >= b >= c or a >= c >= b:
    hypotenus = a
    leg1 = b
    leg2 = c
elif b >= a >= c or b >= c >= a:
    hypotenus = b
    leg1 = a
    leg2 = c
else:
    hypotenus = c
    leg1 = b
    leg2 = a

if hypotenus >= leg1 + leg2:
    print('impossible')
elif hypotenus ** 2 == leg1 ** 2 + leg2 ** 2:
    print('rectangular')
elif hypotenus ** 2 < leg1 ** 2 + leg2 ** 2:
    print('acute')
else:
    print('obtuse')
