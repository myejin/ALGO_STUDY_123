# IIX와 XII는 같으므로 맨처음 시작 idx와 같거나 큰 위치의 숫자만 생각해주면 된다

rom = [1, 5, 10, 50]
n = int(input())
num = [False]*1001


def dfs(idx, all_sum, cnt):
    if cnt == n:
        num[all_sum] = True
        return
    for i in range(idx, 4):
        all_sum += rom[i]
        dfs(i, all_sum, cnt+1)
        all_sum -= rom[i]


dfs(0, 0, 0)
print(len([i for i in num if i]))
