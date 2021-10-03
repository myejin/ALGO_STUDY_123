"""
Title : 리조트
Link : https://www.acmicpc.net/problem/13302
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

price = [10000, 25000, 37000]

# i일에 쿠폰 j개를 가지고 있을 때
# 범위 확인 하지 않기 위한 패딩
dp = [[10 ** 7] * 50 for _ in range(n + 10)]
dp[0][0] = 0

# 1일 >> n일 진행하며 쿠폰 늘리면서 가격 확인
for i in range(n + 1):
    for j in range(41):
        if dp[i][j] != 10 ** 7:
            price = dp[i][j]
            # 다음 날 리조트에 가지 않는 경우
            if i + 1 in arr:
                if dp[i + 1][j] > price:
                    dp[i + 1][j] = price
            # 쿠폰을 사용할 수 있는 경우
            if j >= 3:
                if dp[i + 1][j - 3] > price:
                    dp[i + 1][j - 3] = price
            # 1일권, 3일권, 5일권 구매
            # 3일, 5일권은 그 사이 기간 사용도 같이 표시
            # 1일권
            if dp[i + 1][j] > price + 10000:
                dp[i + 1][j] = price + 10000
            # 3일권
            for d in range(1, 4):
                if dp[i + d][j + 1] > price + 25000:
                    dp[i + d][j + 1] = price + 25000
            # 5일권
            for d in range(1, 6):
                if dp[i + d][j + 2] > price + 37000:
                    dp[i + d][j + 2] = price + 37000

print(min(dp[n]))
