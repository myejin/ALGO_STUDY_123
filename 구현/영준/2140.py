"""
Title : 지뢰찾기
Link : https://www.acmicpc.net/problem/2140
"""

import sys
input = sys.stdin.readline


def check(x: int, y: int) -> bool:
    global game_board
    for d in range(8):
        nx, ny = x + dx[d], y + dy[d]
        if game_board[nx][ny] == '0':
            return True
    return False


def calc(x, y):
    global game_board
    for d in range(8):
        nx, ny = x + dx[d], y + dy[d]
        try:
            n = int(game_board[nx][ny])
            if n > 0:
                game_board[nx][ny] = str(n - 1)
        except Exception:
            continue


if __name__ == '__main__':
    N = int(input())
    game_board = [list(input().strip()) for _ in range(N)]
    dx, dy = (-1, -1, 0, 1, 1, 1, 0, -1), (0, 1, 1, 1, 0, -1, -1, -1, 0)

    if N == 1 or N == 2:
        print(0)
        exit()
    elif N == 3:
        if game_board[0][0] == '0':
            print(0)
        else:
            print(1)
        exit()
    ans = (N - 2) * (N - 2)
    for i in range(1, N - 1):
        if check(i, 1):
            ans -= 1
        else:
            calc(i, 1)
        if check(i, N - 2):
            ans -= 1
        else:
            calc(i, N - 2)
    for i in range(2, N - 2):
        if check(1, i):
            ans -= 1
        else:
            calc(1, i)
        if check(N - 2, i):
            ans -= 1
        else:
            calc(N - 2, i)
    print(ans)

'''
Counter Example
1
0

2
12
01

3
000
0#0
000
'''
