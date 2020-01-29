p = float(input())
x = int(input())
y = int(input())

deposit = x * 100 + y
new_deposit = deposit + ((deposit / 100) * p)
rub = int(new_deposit // 100)
cop = int(new_deposit % 100)

print(rub, cop)
