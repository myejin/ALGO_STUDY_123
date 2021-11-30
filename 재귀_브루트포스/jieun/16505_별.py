N = 2**int(input())

maps = [[' ']*(N) for _ in range(N)]

#분할 정복
def star(x, y, n):
    if n==1:
        maps[x][y] ='*'
        return
    n//=2

    star(x, y, n)
    star(x+n, y, n)
    star(x, y+n, n)

star(0,0,N)

for i in range(len(maps)):
    stst = []
    for j in range(len(maps[0])):
        stst.append(maps[i][j])
    print((''.join(stst)).rstrip())