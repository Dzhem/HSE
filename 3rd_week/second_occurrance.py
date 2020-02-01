s = input()

first_f = s.find('f')
if first_f == -1:
    print(-2)
else:
    new_s = s[first_f + 1:]
    second_f = new_s.find('f')
    if second_f == -1:
        print(second_f)
    else:
        print(first_f + second_f + 1)
