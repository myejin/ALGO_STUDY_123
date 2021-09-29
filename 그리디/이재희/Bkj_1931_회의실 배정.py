import sys
input = sys.stdin.readline

N = int(input().strip())
meet = [list(map(int, input().strip().split())) for _ in range(N)]

# 끝나는 시간과 시작 시간 순서로 정렬
meet = sorted(meet, key=lambda x : (x[1], x[0]))

cnt = 0
idx = 0
time = 0

while idx < N:
    # 시작 시간이 현재 시각 이후일 경우 회의 카운트
    if meet[idx][0] >= time:
        cnt += 1
        time = meet[idx][1]
    idx += 1

print(cnt)