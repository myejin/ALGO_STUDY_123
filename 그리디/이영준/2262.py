"""
Title : 토너먼트 만들기
Link : https://www.acmicpc.net/problem/2262
"""

import sys
input = sys.stdin.readline


N = int(input())
players = list(map(int, input().split()))

gaps = 0
while len(players) > 1:
    last = max(players)
    last_idx = players.index(last)
    
    if last_idx == 0:
        gaps += players[0] - players[1]
    elif last_idx == len(players) - 1:
        gaps += players[-1] - players[-2]
    else:
        if players[last_idx - 1] > players[last_idx + 1]:
            gaps += players[last_idx] - players[last_idx - 1]
        else:
            gaps += players[last_idx] - players[last_idx + 1]
    players = players[:last_idx] + players[last_idx + 1:]

print(gaps)
