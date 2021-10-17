# S1 21608 상어 초등학교
# https://www.acmicpc.net/problem/21608
# 구현
from collections import deque, OrderedDict


def find_pos(lst):
    check = OrderedDict()
    while lst:             # key : 좋아하는 학생 근처에 앉을 수 있는 자리, value: 좋아하는 학생 인접 수
        r, c = lst.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if nr < 0 or nr >= N or nc < 0 or nc >= N or pos[nr][nc]:
                continue
            if (nr, nc) in check:
                check[(nr, nc)] += 1
            else:
                check[(nr, nc)] = 1
    # value 값으로 내림차순하고, nr값, nc 값 순으로 오름차순해줌.
    sort_check = sorted(check.items(), key=lambda x: (-x[1], x[0][0], x[0][1]))
    num = 0
    if len(sort_check) == 0:    # 만약 좋아하는 학생 근처에 앉을 수 없다면 빈자리를 정렬해서 sort_check를 만들어줌.
        for i in range(N):
            for j in range(N):
                if pos[i][j] == 0:
                    check[(i, j)] = 1
    sort_check = sorted(check.items(), key=lambda x: (-x[1], x[0][0], x[0][1]))
    tmp = sort_check[0][1]    # 좋아하는 학생의 인접 수
    for s in range(len(sort_check)):   # 조건 1번을 만족하는 칸이 여러개라면, 그 칸이 몇개인지
        if tmp == sort_check[s][1]:
            num += 1
        else:
            break
    if num == 1:                    # 조건 1
        return sort_check[0][0]
    else:                           # 조건 2, 3
        empty = OrderedDict()       # 조건 1을 만족하는 칸(key) 중에 인접한 칸 중에서 비어있는 칸이 몇개(value)인지 계산.
        for k in range(num):
            temp = 0
            r, c = sort_check[k][0]
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if nr < 0 or nr >= N or nc < 0 or nc >= N or pos[nr][nc]:
                    continue
                temp += 1
            empty[(sort_check[k][0])] = temp
        sort_empty = sorted(empty.items(), key=lambda x: (-x[1], x[0][0], x[0][1]))   # 빈칸은 내림차순, 위치는 오름차순으로 정렬
        return sort_empty[0][0]    # 빈칸이 제일 많고, 같다면 행의 번호가 가장작고 열도 작은 것.


N = int(input())

love = OrderedDict()
order = []
for _ in range(N*N):
    lt = list(map(int, input().split()))
    love[lt[0]] = lt[1:]          # key : 학생번호, value : [좋아하는 학생의 번호]
    order.append(lt[0])           # 학생번호 순서 list


pos = [[0]*N for _ in range(N)]   # 학생 자리 배치

i = 0
sn = order[i]
sr, sc = 1, 1
pos[sr][sc] = sn             # 첫번째 학생은 가장 무조건 (1, 1) 자리에 앉음 ( 문제 기준으론 (2, 2))
student = {sn: (sr, sc)}     # 학생번호 : 학생이 앉은 위치
i += 1
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

while i < N*N:
    nn = order[i]              # 학생의 번호
    stack = deque()            # 좋아하는 학생이 자리에 앉아있을 경우 좋아하는 학생의 위치
    for j in love[nn]:         # 좋아하는 학생의 번호 리스트
        if j in student:
            stack.append(student[j])
    x, y = find_pos(stack)     # 학생이 어디에 앉아야 하는지 구하는 함수
    pos[x][y] = nn
    student[nn] = (x, y)       # 자리에 앉았으므로 추가시켜줌.
    i += 1

# 만족도 구하기
sat = 0
for i in range(N):   # pos 의 (0, 0) 부터 자기 위치에 인접해있는 위치가 만약 자신이 좋아하는 학생의 위치 리스트에 존재한다면 카운트 해줌.
    for j in range(N):
        cnt = 0
        tmp = []
        x, y = student[pos[i][j]]
        for l in love[pos[i][j]]:
            tmp.append(student[l])
        for d in range(4):
            nx = x + dr[d]
            ny = y + dc[d]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if (nx, ny) in tmp:
                cnt += 1
        if cnt == 4:
            sat += 1000
        elif cnt == 3:
            sat += 100
        elif cnt == 2:
            sat += 10
        elif cnt == 1:
            sat += 1

print(sat)

