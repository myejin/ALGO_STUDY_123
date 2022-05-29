"""
Title : 주사위 굴리기 2
Link : https://www.acmicpc.net/problem/23288
"""

from collections import deque
import sys

input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def move(x: int, y: int, d: int) -> tuple:
    match d:
        case 0:
            x -= 1
        case 1:
            y += 1
        case 2:
            x += 1
        case 3:
            y -= 1
    return x, y


def get_points(N: int, M: int, my_map: list) -> list:
    points = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if points[i][j]:
                continue
            queue = deque([(i, j)])
            pos = set()
            num = my_map[i][j]
            while queue:
                x, y = queue.popleft()
                if (x, y) in pos:
                    continue
                pos.add((x, y))
                for d in range(4):
                    nx, ny = move(x, y, d)
                    if 0 <= nx < N and 0 <= ny < M:
                        if my_map[nx][ny] == num and (nx, ny) not in pos:
                            queue.append((nx, ny))
            count = len(list(pos))
            point = count * num
            for x, y in pos:
                points[x][y] = point
    return points


class Dice:
    def __init__(self, N: int, M: int) -> None:
        self.N = N
        self.M = M
        self.x = 0
        self.y = 0
        self.bottom = 6
        self.top = 1
        self.up = 2
        self.down = 5
        self.right = 3
        self.left = 4
        self.direction = 1

    def turn(self, my_map: list, points: list) -> int:
        nx, ny = move(self.x, self.y, self.direction)
        if nx < 0 or nx >= self.N or ny < 0 or ny >= self.M:
            self.direction = (self.direction + 2) % 4
            nx, ny = move(self.x, self.y, self.direction)
        self.x, self.y = nx, ny
        self.move_dice()
        self.turn_direction(self.bottom, my_map[nx][ny])
        return points[nx][ny]

    def move_dice(self) -> None:
        if self.direction == 0:
            self.bottom, self.up, self.top, self.down = (
                self.up,
                self.top,
                self.down,
                self.bottom,
            )
        elif self.direction == 1:
            self.bottom, self.right, self.top, self.left = (
                self.right,
                self.top,
                self.left,
                self.bottom,
            )
        elif self.direction == 2:
            self.bottom, self.up, self.top, self.down = (
                self.down,
                self.bottom,
                self.up,
                self.top,
            )
        elif self.direction == 3:
            self.bottom, self.right, self.top, self.left = (
                self.left,
                self.bottom,
                self.right,
                self.top,
            )

    def turn_direction(self, dice: int, floor: int) -> None:
        if dice > floor:
            self.direction = (self.direction + 1) % 4
        elif dice < floor:
            self.direction = (self.direction - 1) % 4


if __name__ == "__main__":
    N, M, K = MIIS()
    my_map = [list(MIIS()) for _ in range(N)]
    dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
    points = get_points(N, M, my_map)
    ans = 0
    dice = Dice(N, M)
    for _ in range(K):
        ans += dice.turn(my_map, points)
    print(ans)
