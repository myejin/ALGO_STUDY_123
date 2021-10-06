"""
Title : 상어 초등학교
Link : https://www.acmicpc.net/problem/21608
"""

import sys
input = sys.stdin.readline


def search_friends(student: int, friends: list):
    global students_order, students_seat, classroom
    # 친구들의 자리가 이미 정해져있는지
    prob_seat = []
    for f in friends:
        # 친구가 이미 자리 차지하고 있을 때
        if students_seat[f] != []:
            x, y = students_seat[f]
            # 4방향 탐색
            if x > 0 and classroom[x - 1][y] == 0:
                prob_seat.append((x - 1, y))
            if x < n - 1 and classroom[x + 1][y] == 0:
                prob_seat.append((x + 1, y))
            if y > 0 and classroom[x][y -1 ] == 0:
                prob_seat.append((x, y - 1))
            if y < n - 1 and classroom[x][y + 1] == 0:
                prob_seat.append((x, y + 1))            
    return prob_seat


def search_empty_seat():
    global n, classroom
    # 비어있는 자리중 가능성 있는 자리 탐색
    prob_seat = []
    empty_near = 0
    for i in range(n):
        for j in range(n):
            if classroom[i][j] == 0:
                empty = 0
                # 4방향 탐색
                if i > 0 and classroom[i - 1][j] == 0:
                    empty += 1
                if i < n - 1 and classroom[i + 1][j] == 0:
                    empty += 1
                if j > 0 and classroom[i][j -1 ] == 0:
                    empty += 1
                if j < n - 1 and classroom[i][j + 1] == 0:
                    empty += 1
                if empty == 4:
                    return i, j
                elif prob_seat == []:
                    empty_near = empty
                    prob_seat = [i, j]
                elif empty > empty_near:
                    empty_near = empty
                    prob_seat = [i, j]
    return prob_seat


def find_best_seat(prob_seat):
    global n, classroom
    # 가능한 자리 중 조건에 맞는 최적 자리
    seat = []
    friends_count = 0
    empty_near = 0
    for i in range(len(prob_seat)):
        friends_near = 0
        for j in range(i, len(prob_seat)):
            if prob_seat[i] == prob_seat[j]:
                friends_near += 1
        # 다른 자리보다 친구 수가 주변에 적으면
        if friends_near < friends_count:
            continue
        # 주변 빈자리 탐색
        x, y = prob_seat[i]
        empty = 0
        # 4방향 탐색 
        if x > 0 and classroom[x - 1][y] == 0:
            empty += 1
        if x < n - 1 and classroom[x + 1][y] == 0:
            empty += 1
        if y > 0 and classroom[x][y -1 ] == 0:
            empty += 1
        if y < n - 1 and classroom[x][y + 1] == 0:
            empty += 1
        # 아직 자리가 비어있을 때
        if seat == []:
            seat = x, y
            friends_count = friends_near
            empty_near = empty
        # 다른 자리보다 친구 수가 더 많으면 변경
        if friends_near > friends_count:
            friends_count = friends_near
            seat = [x, y]
            empty_near = empty
        # 친구수가 같다면, 비어 있는 칸 확인
        else:
            # 주변 빈자리가 더 많다면 교체
            if empty > empty_near:
                seat = [x, y]
                empty_near = empty
            # 주변 빈 자리가 같으면 더 왼쪽 더 위쪽 일때 교체
            elif empty == empty_near:
                if x < seat[0] or (x == seat[0] and y < seat[1]):
                    seat = [x, y]
    return seat


def count_happiness(classroom) -> int:
    global students_order, students_seat
    happiness = 0
    for student, *friends in students_order:
        # 인접 자리 친구
        friends_near_count = 0
        student_pos = students_seat[student]
        for f in friends:
            if abs(student_pos[0] - students_seat[f][0]) + abs(student_pos[1] - students_seat[f][1]) == 1:
                friends_near_count += 1
        # 인접 친구 수에 따라 점수 부여
        if friends_near_count == 1:
            happiness += 1
        elif friends_near_count == 2:
            happiness += 10
        elif friends_near_count == 3:
            happiness += 100
        elif friends_near_count == 4:
            happiness += 1000
    return happiness


n = int(input())
# 학생 자리 배치 순서
students_order = [tuple(map(int, input().split())) for _ in range(n ** 2)]
# 각 학생의 자리
students_seat = [[] for _ in range(n ** 2 + 1)]
# 교실
classroom = [[0] * n for _ in range(n)]

# 첫 학생부터 자리 채우기
for student, *friends in students_order:
    # 친구들 기준 가능한 자리가 있는지
    prob_seat = search_friends(student, friends)
    # 친구들 기준 가능한 자리 없을 때
    if prob_seat == []:
        # 빈 자리중 가능한 빈자리 탐색
        x, y = search_empty_seat()
        classroom[x][y] = student
        students_seat[student] = [x, y]
    # 친구들 기준 가능한 자리 있을 때
    else:
        # 받은 가능한 자리 중 최선의 자리 선택
        x, y = find_best_seat(prob_seat)
        classroom[x][y] = student
        students_seat[student] = [x, y]

print(count_happiness(classroom))
