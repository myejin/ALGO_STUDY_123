"""
Title : 스트릿 코딩 파이터
Link : https://www.acmicpc.net/problem/23348
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


A, B, C = MIIS()
max_team_score = 0

for _ in range(int(input())):
    team_score = 0
    for _ in range(3):
        a, b, c = MIIS()
        team_score += a * A + b * B + c * C
    if team_score > max_team_score:
        max_team_score = team_score

print(max_team_score)
