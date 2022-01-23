import sys
from collections import deque
input = sys.stdin.readline

def dfs(now_idx, student_lst, student_cnt, Y_cnt):
    global result
    # 선택된 학생의 수가 7명일 경우
    if student_cnt >= 7:
        # bfs 탐색으로 모두 인접한 경우 카운트
        if adjacent_check(student_lst):
            result += 1
        return
    # 현재 인덱스의 다음부터 선택될 수 있는 인덱스까지 탐색
    for idx in range(now_idx + 1, 19 + student_cnt):
        x = idx // 5
        y = idx % 5
        # 선택된 학생이 '임도연파' 인 경우
        if grid[x][y] == 'Y':
            # 이미 '임도연파' 가 3명 이상인 경우 return
            if Y_cnt >= 3:
                continue
            # 아닌 경우 '임도연파'의 수를 증가하면서 탐색
            else:
                dfs(idx, student_lst + [[x, y]], student_cnt + 1, Y_cnt + 1)
        # 아닌 경우 바로 탐색
        else:
            dfs(idx, student_lst + [[x, y]], student_cnt + 1, Y_cnt)
        

def adjacent_check(student_lst):
    # 처음 선택된 학생부터 bfs 탐색
    sx, sy = student_lst[0]
    checked = [[0]*5 for _ in range(5)]
    checked[sx][sy] = 1
    # 인접한 학생의 수 카운트
    adjacent_student_cnt = 0
    deq = deque([[sx, sy]])
    while deq:
        x, y = deq.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # 선택된 학생이면서 체크하지 않았을 경우
            if [nx, ny] in student_lst and not checked[nx][ny]:
                checked[nx][ny] = 1
                deq.append([nx, ny])
                adjacent_student_cnt += 1
    # 인접한 학생이 6명(모두 인접)일 경우 True 반환
    if adjacent_student_cnt >= 6:
        return True
    else:
        return False

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

grid = [list(str(input().strip())) for _ in range(5)]

result = 0

dfs(-1, [], 0, 0)

print(result)