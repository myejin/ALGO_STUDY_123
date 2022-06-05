"""
Title : 축구
Link : https://www.acmicpc.net/problem/1344
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    A, B = int(input()), int(input())
    A, B = A / 100, B / 100
    dp = [[[0] * 19 for _ in range(19)] for _ in range(19)]
    dp[1][0][0] = (1 - A) * (1 - B)
    dp[1][0][1] = (1 - A) * B
    dp[1][1][0] = A * (1 - B)
    dp[1][1][1] = A * B
    for match in range(2, 19):
        for i in range(match + 1):
            for j in range(match + 1):
                dp[match][i][j] = dp[match - 1][i][j] * (1 - A) * (1 - B)
                if i > 0:
                    dp[match][i][j] += dp[match - 1][i - 1][j] * A * (1 - B)
                if j > 0:
                    dp[match][i][j] += dp[match - 1][i][j - 1] * (1 - A) * B
                if i > 0 and j > 0:
                    dp[match][i][j] += dp[match - 1][i - 1][j - 1] * A * B
    result = 0
    primes = {2, 3, 5, 7, 11, 13, 17}
    for i in range(19):
        for j in range(19):
            if i in primes or j in primes:
                result += dp[18][i][j]
    print(result)
