"""
Title : 졸업 사진
Link : https://www.acmicpc.net/problem/23349
"""

import sys
input = sys.stdin.readline


places = dict()
students = set()

for _ in range(int(input())):
    name, place, st, end = input().strip().split()
    if name in students:
        continue
    students.add(name)
    if place in places:
        places[place].append((int(st), int(end)))
    else:
        places[place] = [(int(st), int(end))]

notice_place = ''
notice_time = []
reserv_people_count = 0

for place in places:
    reserv_times = sorted(places[place], key=lambda x:x[1])
    l = len(reserv_times)
    for i in range(l):
        # i번째 인덱스 기준으로 최대로 겹치는 예약 시간 탐색
        s, e = reserv_times[i]
        people_count = 1
        for j in range(i + 1, l):
            # 시작 시간이 겹치면 사람 ++
            # 시간 조정 필요하면 조정
            if reserv_times[j][0] < e:
                people_count += 1
                if s < reserv_times[j][0]:
                    s = reserv_times[j][0]
        # 더 많은 사람이 원하는 시간인지
        if people_count > reserv_people_count:
            notice_place = place
            notice_time = [s, e]
            reserv_people_count = people_count
        # 사람 수가 같다면 장소 사전순
        elif people_count == reserv_people_count:
            if place < notice_place:
                notice_place = place
                notice_time = [s, e]
                reserv_people_count = people_count
            # 빠른 시간 우선 탐색했으므로 추가 조건문 필요 ㄴㄴ

print(notice_place, *notice_time)
