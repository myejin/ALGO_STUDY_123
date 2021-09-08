"""
Title : ATM
Link : https://www.acmicpc.net/problem/11399
"""

n = int(input())
time = sorted(list(map(int, input().split())))

ans = 0
for i in range(n):
    ans += time[i] * (n - i)

print(ans)
