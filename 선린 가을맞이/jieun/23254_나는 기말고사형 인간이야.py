import sys
import heapq
input = sys.stdin.readline
N, M = map(int, input().split())
N *= 24
A = list(map(int, input().split()))
B = list(map(int, input().split()))
myq = []
# 일단 하나도 공부하지 않아도 얻을 수 있는 점수
ans = sum(A)


for i in range(M):
    # 한 시간 공부할 때마다 b점 오름
    if A[i] < 100:
        heapq.heappush(myq, [-min(B[i], 100-A[i], 100 - A[i]), -(100-A[i])])

#heapify

while N > 0 and myq:
    a, b = heapq.heappop(myq)
    a = -a
    b = -b
    now = min(b//a, N)
    ans += now * a
    N -= now
    if (b - now * a > 0):
        b -= now * a
        a = b
        heapq.heappush(myq, [-a, -b])

print(ans)