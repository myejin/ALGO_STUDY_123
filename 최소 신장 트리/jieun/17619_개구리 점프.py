import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
arr = [list(map(int, input().split())) + [i] for i in range(N)]
arr.sort(key=lambda x: x[0]) # 통나무 정렬
p = [i for i in range(N)] # 부모

p_idx = arr[0][3] # 처음에 위치한 통나무의 idx
x_end = arr[0][1] # 처음에 위치한 통나무의 제일 끝 부분

for i in range(1, N):
    # 이전 통나무의 제일 끝부분 x좌표보다 현재 통나무의 제일 첫부분 x좌표가 작으면 점프로 이동 가능
    # 부모가 같다 (같은 팀이다)
    # 현재 본 통나무의 제일 끝부분과 이전 통나무 제일 끝부분 중 더 긴 것으로 갱신
    if x_end >= arr[i][0]:
        x_end = max(x_end, arr[i][1])
        p[arr[i][3]] = p_idx
    # 아니라면 이동 불가능, 서로 다른 부모
    else:
        p_idx = arr[i][3]
        x_end = arr[i][1]

for _ in range(Q):
    x, y = map(int, input().split())
    if p[x-1] == p[y-1]: # 부모가 같음 == 점프 가능
        print(1)
    else:
        print(0)