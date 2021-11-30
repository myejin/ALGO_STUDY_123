# 비어 있는 칸 중에 좋아하는 학생이 인접한 칸에 가장 많은 칸
# 여러 개이면 비어있는 칸이 가장 많은 칸
# 여러개이면 행의 번호가 가장 작은 칸, 그러한 칸도 여러 개 이면 열의 변호가 작은 칸
n = int(input())

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def find_desk(person):
    max_friend = -1
    max_empty = -1
    person_r = -1
    person_c = -1

    for i in range(n):
        for j in range(n):
            empty_desk = 0
            love_friend = 0
            if not desk[i][j]:
                for k in range(4):
                    ny = i + dy[k]
                    nx = j + dx[k]
                    if 0 <= ny < n and 0 <= nx < n:
                        if desk[ny][nx] in students[person]:
                            love_friend += 1
                        if not desk[ny][nx]:
                            empty_desk += 1
                if max_friend == love_friend:
                    if max_empty < empty_desk:
                        person_r = i
                        person_c = j
                        max_friend = love_friend
                        max_empty = empty_desk
                elif max_friend < love_friend:
                    person_r = i
                    person_c = j
                    max_friend = love_friend
                    max_empty = empty_desk
    return person_r, person_c


input_students = [list(map(int, input().split())) for _ in range(n*n)]
desk = [[0]*n for _ in range(n)]
students = {}
for student in input_students:
    students[student[0]] = set(student[1:])
    y, x = find_desk(student[0])
    desk[y][x] = student[0]

ans = 0

for i in range(n):
    for j in range(n):
        temp = 0
        for k in range(4):
            ny = i + dy[k]
            nx = j + dx[k]
            if 0 <= ny < n and 0 <= nx < n and (desk[ny][nx] in students[desk[i][j]]):
                temp += 1
        if temp == 1:
            ans += 1
        elif temp == 2:
            ans += 10
        elif temp == 3:
            ans += 100
        elif temp == 4:
            ans += 1000
print(ans)