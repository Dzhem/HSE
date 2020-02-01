s = input()

first_h = s.find('h')
last_h = len(s) - s[::-1].find('h') - 1

new_s = s[:first_h] + s[last_h + 1:]
print(new_s)
