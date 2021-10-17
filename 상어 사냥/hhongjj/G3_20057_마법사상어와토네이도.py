# G3 20057 마법사 상어와 토네이도
# https://www.acmicpc.net/problem/20057
# 구현, 시뮬레이션
import sys
input = sys.stdin.readline


# 좌표 이동 방향 찾기
def find_out_direction(er, ec, d):
    if d == 0:
        return er, ec - 1
    elif d == 1:
        return er + 1, ec
    elif d == 2:
        return er, ec + 1
    else:
        return er - 1, ec

# 그걸 토대로 모래 비율 방향도 바꿔 옮기기
def move_sand(er, ec, d):
    now = sand[er][ec]
    sand[er][ec] = 0      # y 이므로 0으로 바꿈.
    # 방향에 따른 모래 비율 (0:좌, 1:하, 2:우, 3:상)
    in_sum, out_sum = 0, 0
    for i in range(5):
        for j in range(5):
            x, y = er-2+i, ec-2+j   # 모래가 이동할 좌표
            if d_list[d][i][j] == 'a':  # 마지막 남은 모래 저장.
                ax, ay = x, y
                continue
            if x < 0 or x >= N or y < 0 or y >= N:     # 이동할 좌표가 범위를 벗어난다면
                out_sum += now * d_list[d][i][j] // 100
                continue
            else:
                sand[x][y] += now * d_list[d][i][j] // 100
                in_sum += now * d_list[d][i][j] // 100
    if N > ax >= 0 and N > ay >= 0:
        sand[ax][ay] += now - in_sum - out_sum
    return


N = int(input())
sand = list(list(map(int, input().split())) for _ in range(N))
nr, nc = N//2, N//2  # 시작 지점은 항상 정중앙
d_list = [[[0, 0, 2, 0, 0], [0, 10, 7, 1, 0], [5, 'a', 0, 0, 0], [0, 10, 7, 1, 0], [0, 0, 2, 0, 0]],
          [[0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [2, 7, 0, 7, 2], [0, 10, 'a', 10, 0], [0, 0, 5, 0, 0]],
          [[0, 0, 2, 0, 0], [0, 1, 7, 10, 0], [0, 0, 0, 'a', 5], [0, 1, 7, 10, 0], [0, 0, 2, 0, 0]],
          [[0, 0, 5, 0, 0], [0, 10, 'a', 10, 0], [2, 7, 0, 7, 2], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]]

before = sum(map(sum, sand))
num, d = 1, -1
# 화살표 방향이 2번씩 같은 개수로 매번 바뀌는 걸로 계산함.
while num < N:
    for i in range(2):
        d = (d + 1) % 4
        for j in range(num):
            nr, nc = find_out_direction(nr, nc, d)
            move_sand(nr, nc, d)
    num += 1
d = (d + 1) % 4
for j in range(num):
    nr, nc = find_out_direction(nr, nc, d)
    move_sand(nr, nc, d)

after = sum(map(sum, sand))
print(before - after)


# 약간 다른 방법으로, 행렬의 구역에 따라 방향을 나눔
# 좌표 이동 방향 찾기
# def find_out_direction(er, ec):
#     if er == ec and er <= N // 2:              # 왼쪽 위 대각선 -> 좌
#         return er, ec - 1, 0
#     elif er == ec and er > N // 2:             # 오른쪽 아래 대각선 -> 상
#         return er - 1, ec, 3
#     elif er + ec + 1 == N:
#         if er > N // 2:                        # 왼쪽 아래 대각선 -> 우
#             return er, ec + 1, 2
#         else:                                  # 오른쪽 위 대각선 -> 좌
#             return er, ec - 1, 0
#     elif er < ec:
#         if er + ec < N - 1:                    # 위쪽 부분 대각선 사이 -> 좌
#             return er, ec - 1, 0
#         else:                                  # 오른쪽 부분 대각선 사이 -> 상
#             return er - 1, ec, 3
#     elif er > ec:
#         if er + ec < N - 1:                    # 왼쪽 부분 대각선 사이 -> 하
#             return er + 1, ec, 1
#         else:                                  # 아래쪽 부분 대각선 사이 -> 우
#             return er, ec + 1, 2
#
# # 그걸 토대로 모래 비율 방향도 바꿔 옮기기
# def move_sand(er, ec, d):
#     now = sand[er][ec]
#     sand[er][ec] = 0      # y 이므로 0으로 바꿈.
#     # 방향에 따른 모래 비율 (0:좌, 1:하, 2:우, 3:상)
#     in_sum, out_sum = 0, 0
#     for i in range(5):
#         for j in range(5):
#             x, y = er-2+i, ec-2+j   # 모래가 이동할 좌표
#             if d_list[d][i][j] == 'a':  # 마지막 남은 모래 저장.
#                 ax, ay = x, y
#                 continue
#             if x < 0 or x >= N or y < 0 or y >= N:
#                 out_sum += now * d_list[d][i][j] // 100
#                 continue
#             else:
#                 sand[x][y] += now * d_list[d][i][j] // 100
#                 in_sum += now * d_list[d][i][j] // 100
#     if N > ax >= 0 and N > ay >= 0:
#         sand[ax][ay] += now - in_sum - out_sum
#     return
#
# N = int(input())
# sand = list(list(map(int, input().split())) for _ in range(N))
# nr, nc = N//2, N//2  # 시작 지점은 항상 정중앙
# dr = [0, 1, 0, -1]  # 방향만 (0:좌, 1:하, 2:우, 3:상)
# dc = [-1, 0, 1, 0]
# d_list = [[[0, 0, 2, 0, 0], [0, 10, 7, 1, 0], [5, 'a', 0, 0, 0], [0, 10, 7, 1, 0], [0, 0, 2, 0, 0]],
#           [[0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [2, 7, 0, 7, 2], [0, 10, 'a', 10, 0], [0, 0, 5, 0, 0]],
#           [[0, 0, 2, 0, 0], [0, 1, 7, 10, 0], [0, 0, 0, 'a', 5], [0, 1, 7, 10, 0], [0, 0, 2, 0, 0]],
#           [[0, 0, 5, 0, 0], [0, 10, 'a', 10, 0], [2, 7, 0, 7, 2], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]]
#
# before = sum(map(sum, sand))
# while nr != 0 or nc != 0:
#     nr, nc, d = find_out_direction(nr, nc)   # 옮겨진 좌표와 방향
#     move_sand(nr, nc, d)
#
# after = sum(map(sum, sand))
# print(before - after)

# 이게 더 빠를 줄 알았는데 더 느림
# if er < ec:
#     if er + ec < N - 1:  # 위쪽 부분 대각선 사이 -> 좌
#         return er, ec - 1, 0
#     elif er + ec > N - 1:  # 오른쪽 부분 대각선 사이 -> 상
#         return er - 1, ec, 3
#     else:  # 오른쪽 위 대각선 -> 좌
#         return er, ec - 1, 0
# elif er > ec:
#     if er + ec < N - 1:  # 왼쪽 부분 대각선 사이 -> 하
#         return er + 1, ec, 1
#     elif er + ec > N - 1:  # 아래쪽 부분 대각선 사이 -> 우
#         return er, ec + 1, 2
#     else:  # 왼쪽 아래 대각선 -> 우
#         return er, ec + 1, 2
# else:
#     if er <= N // 2:  # 왼쪽 위 대각선 -> 좌
#         return er, ec - 1, 0
#     else:  # 오른쪽 아래 대각선 -> 상
#         return er - 1, ec, 3
