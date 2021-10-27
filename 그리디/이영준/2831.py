"""
Title : 댄스 파티
Link : https://www.acmicpc.net/problem/2831
"""

import sys
input = sys.stdin.readline


n = int(input())

boys_upper = []
boys_lower = []
boys = list(map(int, input().split()))
for height in boys:
    if height > 0:
        boys_upper.append(height)
    else:
        boys_lower.append(-1 * height)

girls_upper = []
girls_lower = []
girls = list(map(int, input().split()))
for height in girls:
    if height > 0:
        girls_upper.append(height)
    else:
        girls_lower.append(-1 * height)

group_count = 0
# 자기보다 키 큰 여자 / 키 작은 남자
boys_upper.sort()
girls_lower.sort()
boy_idx = girl_idx = 0
while True:
    if boy_idx == len(boys_upper) or girl_idx == len(girls_lower):
        break
    # 조건 성립
    if boys_upper[boy_idx] < girls_lower[girl_idx]:
        group_count += 1
        boy_idx += 1
        girl_idx += 1
    # 아니라면 남자키가 같거나 더 큼
    else:
        girl_idx += 1

# 자기보다 키 작은 여자 / 키 큰 남자
boys_lower.sort()
girls_upper.sort()
boy_idx = girl_idx = 0
while True:
    if boy_idx == len(boys_lower) or girl_idx == len(girls_upper):
        break
    # 조건 성립
    if boys_lower[boy_idx] > girls_upper[girl_idx]:
        group_count += 1
        boy_idx += 1
        girl_idx += 1
    # 아니라면 여자키가 같거나 더 큼
    else:
        boy_idx += 1

print(group_count)
