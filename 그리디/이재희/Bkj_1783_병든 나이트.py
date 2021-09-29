from collections import deque

N, M = map(int, input().split())

dx = [-2, -1, 1, 2]
dy = [1, 2, 2, 1]

deq = deque()
result = 0
check = False  # 이동 방법을 한 번씩 사용할 수 있는지 확인

deq.append([N-1, 0, 1])

while deq:
    a = deq.popleft()
    i, j, cnt = a[0], a[1], a[2]

    # 방문한 칸이 5개인 경우 노드 탐색을 중지
    if cnt >= 5:
        # 이동 방법을 한 번씩 사용한 도착지인지 확인
        if i == N-1 and j == 6:
            check = True
        continue

    result = max(result, cnt)

    for d in range(4):
        x = i + dx[d]
        y = j + dy[d]
        if 0 <= x < N and 0 <= y < M:
            deq.append([x, y, cnt+1])

# 이동 방법을 한 번씩 사용했을 경우, 체스판의 남은 가로 길이(M-7) 만큼 더해서 비교
if check:
    result = max(result, M-7+5)

print(result)