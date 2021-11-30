from copy import deepcopy
import sys
input = sys.stdin.readline


dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]


def shark_move(shark_y, shark_x, eat_fish, fish_map, fish_dict):
    global ans
    new_maps = deepcopy(fish_map)
    new_dict = deepcopy(fish_dict)

    shark_dir = new_maps[shark_y][shark_x][1]
    shark_eat = new_maps[shark_y][shark_x][0]
    new_dict[shark_eat], new_maps[shark_y][shark_x] = [], []

    ans = max(eat_fish+shark_eat, ans)

    fish_move(shark_y, shark_x, new_maps, new_dict)
    temp_y, temp_x = shark_y, shark_x
    for k in range(1, 4):
        ny, nx = temp_y + dy[shark_dir], temp_x+dx[shark_dir]
        if 0 <= nx < 4 and 0 <= ny < 4 and new_maps[ny][nx]:
            shark_move(ny, nx, eat_fish + shark_eat, new_maps, new_dict)
        temp_y, temp_x = ny, nx


def fish_move(sy, sx, fish_map, fish_dict):
    for idx in range(1, 17):
        if fish_dict[idx]:
            y, x = fish_dict[idx][0], fish_dict[idx][1]
            fish_d = fish_map[y][x][1]
            for k in range(8):
                new_d = (fish_d + k) % 8
                ny = y + dy[new_d]
                nx = x + dx[new_d]
                if 0 <= ny < 4 and 0 <= nx < 4 and (ny, nx) != (sy, sx):
                    fish_map[y][x][1] = new_d
                    if fish_map[ny][nx]:
                        fish_dict[fish_map[ny][nx][0]] = [y, x]
                    fish_dict[idx] = [ny, nx]
                    fish_map[ny][nx], fish_map[y][x] = fish_map[y][x], fish_map[ny][nx]
                    break


input_data = [list(map(int, input().split())) for _ in range(4)]
maps = [[], [], [], []]
fish = {}
ans = 0

# 물고기,
for i in range(4):
    for j in range(0, 8, 2):
        maps[i].append([input_data[i][j], input_data[i][j+1]-1])
        fish[input_data[i][j]] = [i, j//2]


shark_move(0, 0, 0, maps, fish)
print(ans)
