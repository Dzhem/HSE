n = int(input())
u_n = n % 10
word_cows = ''

if n != 11 and u_n == 1:
    word_cows = 'korova'
elif (n != 12 and n != 13 and n != 14) and (u_n == 2 or u_n == 3 or u_n == 4):
    word_cows = 'korovy'
else:
    word_cows = 'korov'

print(n, word_cows)
