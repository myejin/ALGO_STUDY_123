import sys
input = sys.stdin.readline
n = int(input())
paper = [[0]*101 for _ in range(101)]


def find_rec(x, y):
    find_max_size = 100
    for r in range(100):
        if x + r > 100:
            break
        for c in range(100):
            if y + c > 100:
                break
            find_max_size = max(find_max_size, cal_rec(x, y, x+r, y+c))
    return find_max_size


def cal_rec(x, y, h, w):
    cnt = 0
    for k in range(x, h+1):
        for l in range(y, w+1):
            if not paper[k][l]:
                return 0
            else :
                cnt += 1
    return cnt


for _ in range(n):
    a, b = map(int, input().split())
    for i in range(10):
        for j in range(10):
            paper[a+i][b+j] = 1

max_size = 100
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            max_size = max(max_size, find_rec(i, j))

print(max_size)
