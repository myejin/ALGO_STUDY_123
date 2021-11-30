n = int(input())
cnt = 0
money = 1000-n

coin = [500, 100, 50, 10, 5, 1]

for i in range(6):
    cnt += money//coin[i]
    money%=coin[i]

print(cnt)