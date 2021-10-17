# G3 19237 어른 상어
# https://www.acmicpc.net/problem/19237
# 구현, 시뮬레이션

# 상어 이동
def move_shark():
    pre = {}            # 같은 곳으로 이동하는지 확인, {(2, 3): 4, (0, 3): 3, (1, 2): 2, (2, 1): 1}
    move = [0] * (M+1)  # 빈 곳으로 이동했는지 확인
    delete_shark = []
    self_smell = list([] for _ in range(M+1))             # 자신의 냄새가 있는 위치
    # 어디로 이동하는 지
    for n in range(M, 0, -1):                             # 우선 순위가 낮은 상어부터 이동
        d = d_list[n-1]                                   # 각 상어의 방향
        if now_shark[n] == 0:                             # 삭제된 상어라면 now_shark 에서 0이라 넘김
            continue
        er, ec = now_shark[n]                             # 이동해야하는 상어의 위치
        idx = 0                                           # 방향 우선순위
        for t in range(4):
            l = priority[n-1][d-1][t]                     # priority[상어의 번호][상어의 방향][우선순위]
            nr, nc = er + dr[l-1], ec + dc[l-1]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if shark[nr][nc] == 0:                        # 빈칸이라면
                if (nr, nc) in pre.keys():                # 만약에 같은 곳으로 이동하는 상어 있으면 삭제할 것이기 때문에 삭제 될 상어의 번호를 저장.
                    delete_shark.append(pre[(nr, nc)])
                pre[(nr, nc)] = n                         # 움직일 위치 저장 -> 같은 곳에 가면 번호가 높은 상어가 삭제
                move[n] = 1                               # 상어가 움직였는지 확인
                d_list[n-1] = l                           # 상어의 방향 바꿈.
                break
            else:                                         # 빈칸이 아니면 idx +1 해줌
                idx = (idx + 1) % 4
                if shark[nr][nc][0] == n:                 # 빈칸이 없으면 자기자신으로 이동해야하니까 self_smell 에 위치와 방향을 저장.
                    self_smell[n].append((nr, nc, l))
    # 이동하면서 삭제될 상어 now_shark 와 d_list, move 다 0으로 바꿔줌.
    for k in range(len(delete_shark)):
        n = delete_shark[k]
        now_shark[n] = 0
        move[n] = 0
        d_list[n-1] = 0
    len_now = 0  # 현재 살아있는 상어 수
    for k in range(1, len(now_shark)):
        if now_shark[k] != 0:
            len_now += 1
    # 인근에 빈 곳이 없던 상어 자기 냄새칸으로 이동.
    if sum(move) != len_now:                              # move 는 빈칸으로 이동한 상어만 1임.
        for m in range(1, len(move)):
            if move[m] == 0 and now_shark[m] != 0:        # 살아있지만 이동못 한 상어
                r, c, d = self_smell[m][0]                # 자기 냄새를 위에서 우선순위대로 저장했으므로 맨 앞의 위치로 이동.
                pre[(r, c)] = m
                move[m] = 1
                d_list[m-1] = d
    # 이전에 냄새들 하나씩 뺴줌
    change_smell()
    # 이동시킴
    for p, n in pre.items():
        r, c = p
        shark[r][c] = (n, K)
        now_shark[n] = (r, c)
        stack.append((r, c))
    return len_now


def change_smell():
    global stack      # 왜 글로벌?
    stack = list(set(stack))                             # set 을 이용해 다시 자기 냄새로 이동했던 경우를 빼줌.
    delete = []
    for s in range(len(stack)):
        x, y = stack[s]
        if shark[x][y][1] - 1:                           # 냄새가 2 이상이면, 하나 줄여줌.
            shark[x][y] = (shark[x][y][0], shark[x][y][1] - 1)
        else:                                            # 냄새가 1이면 0으로 만들어주고, stack 에서 삭제하기 위해 저장
            shark[x][y] = 0
            delete.append(s)
    for k in range(len(delete)-1, -1, -1):               # stack 뒤에서부터 delete 에 들어있는 위치 삭제함.
        del stack[delete[k]]
    return


N, M, K = map(int, input().split())
shark = list(list(map(int, input().split())) for _ in range(N))  # 상어의 영역
d_list = list(map(int, input().split()))  # 상어의 방향
priority = list(list(list(map(int, input().split())) for _ in range(4)) for _ in range(M))   # 각 상어의 방향 우선순위
dr = [-1, 1, 0, 0]  # 상, 하, 좌, 우
dc = [0, 0, -1, 1]
now_shark = [0]*(M + 1)  # 각 상어의 최신 위치
stack = []  # 남아있는 냄새 체크
for i in range(N):
    for j in range(N):
        if shark[i][j]:
            now_shark[shark[i][j]] = (i, j)  # 각 상어의 번호에 최신 위치
            shark[i][j] = (shark[i][j], K)   # (상어의 번호와, 냄새)
            stack.append((i, j))
# shark [[0, 0, 0, 0, (3, 4)], [0, (2, 4), 0, 0, 0], [(1, 4), 0, 0, 0, (4, 4)], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# now_shark [0, (2, 0), (1, 1), (0, 4), (2, 4)]
# stack [(0, 4), (1, 1), (2, 0), (2, 4)]
sec = 0
res = M
while res > 1 and sec <= 1000:  # 1번 상어만 남거나 1000초가 지나거나
    sec += 1
    res = move_shark()

if sec <= 1000:
    print(sec)
else:
    print(-1)

