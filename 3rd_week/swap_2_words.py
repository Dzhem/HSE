s = input()

index_space = s.find(' ')
first_word = s[:index_space]
second_word = s[index_space + 1:]
new_s = second_word + ' ' + first_word

print(new_s)
