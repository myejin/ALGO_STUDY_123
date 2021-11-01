"""
Title : 나는 기말고사형 인간이야
Link : https://www.acmicpc.net/problem/23254
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())

N, M = MIIS()
grade_now = list(MIIS())
grade_upgrade = list(MIIS())

# 총 남은 시간
time_left = 24 * N
# 한번에 올릴 점수, 시행 횟수, 인덱스
grade_upgrade_by_idx = []
for idx, upgrade in enumerate(grade_upgrade):
    if 100 - grade_now[idx] >= upgrade:
        grade_upgrade_by_idx.append((upgrade, (100 - grade_now[idx]) // upgrade ,idx))
    if (100 - grade_now[idx]) % upgrade:
        grade_upgrade_by_idx.append(((100 - grade_now[idx]) % upgrade, 1, idx))
grade_upgrade_by_idx.sort(key=lambda x: -x[0])

for upgrade, time, idx in grade_upgrade_by_idx:
    if time > time_left:
        grade_now[idx] += upgrade * time_left
        break
    else:
        time_left -= time
        grade_now[idx] += upgrade * time

print(sum(grade_now))


'''
import heapq
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


N, M = MIIS()
grade_now = list(MIIS())
grade_upgrade = list(MIIS())

# 총 남은 시간
time_left = 24 * N
# 많이 올릴 수 있는 점수부터
grade_upgrade_by_idx = []
for idx, upgrade in enumerate(grade_upgrade):
    if 100 - grade_now[idx] >= upgrade:
        grade_upgrade_by_idx.append((-upgrade, idx))
    else:
        grade_upgrade_by_idx.append((-(100 - grade_now[idx]), idx))
heapq.heapify(grade_upgrade_by_idx)

while grade_upgrade_by_idx and time_left:
    upgrade, idx = heapq.heappop(grade_upgrade_by_idx)
    upgrade *= -1
    if grade_now[idx] + upgrade == 100:
        time_left -= 1
        grade_now[idx] = 100
    else:
        max_time_spend = (100 - grade_now[idx]) // upgrade
        if max_time_spend > time_left:
            grade_now[idx] += upgrade * time_left
            time_left = 0
        else:
            grade_now[idx] += upgrade * max_time_spend
            time_left -= max_time_spend
            if 100 - grade_now[idx] > 0:
                heapq.heappush(grade_upgrade_by_idx, (-(100 - grade_now[idx]), idx))

print(sum(grade_now))
'''
