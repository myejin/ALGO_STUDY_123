import sys
input = sys.stdin.readline
N, M = map(int, input().split())
days_money = []
for i in range(N):
    days_money.append(int(input()))

# 한번 꺼낼 때 K원을 인출하고, M번 꺼낼 수 있음. -> K원을 구함
# 최소 금액 -> 하루에 쓰는 금액 중 max, 최대 금액 -> 전체 쓸 금액 합
start = max(days_money)
end = sum(days_money)
K = 0
while start<=end :
    mid = (start+end)//2
    cnt = 0
    left = 0
    for money in days_money:
        if left < money :
            cnt +=1
            left = mid
        left -= money

    if cnt > M :
        start = mid + 1
    else : # M보다 작을 경우 (넣었다 뺏다 해주면서 M을 맞춰줄 수 있는 경우임)
        K = mid
        end = mid - 1 # 더 작은 K값을 찾기 위해 계속 탐색

print(K)
