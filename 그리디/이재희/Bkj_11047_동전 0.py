import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
A = [int(input().strip()) for _ in range(N)]

cnt = 0

# 임의의 수 보다 작은 수들은 약수로 구성되어 있기 때문에, 높은 수부터 탐색 (오름차순이니 뒤에서부터)
for i in range(N-1, -1, -1):
    if K >= A[i]:
        cnt += K//A[i]
        K = K % A[i]

print(cnt)