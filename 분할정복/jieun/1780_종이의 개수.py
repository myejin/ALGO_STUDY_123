import sys
input = sys.stdin.readline

def check(r, c, m):
    origin = paper_table[r][c]
    for i in range(r, r+m):
        for j in range(c, c+m):
            if origin != paper_table[i][j]:
                new_m = m//3
                for ni in range(3):
                    for nj in range(3):
                        check(r + ni*new_m, c + nj*new_m, new_m)
                return
    paper[origin] += 1


n = int(input())
paper_table = [list(map(int, input().split())) for _ in range(n)]
paper = [0, 0, 0] # 0개수 1개수 -1개수
# 같은 수 체크
# 종이 9개로 자르기
check(0,0,n)
for i in range(-1, 2):
    print(paper[i])