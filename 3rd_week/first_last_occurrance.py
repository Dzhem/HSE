s = input()

first_f = s.find('f')
if first_f != -1:
    last_f = len(s) - s[::-1].find('f') - 1
    if first_f != last_f:
        print(first_f, last_f)
    else:
        print(first_f)
