"""
Title : 여우는 어떻게 울지?
Link : https://www.acmicpc.net/problem/9536
"""

import sys
input = sys.stdin.readline


for _ in range(int(input())):
    record = list(input().strip().split())
    # record의 각 소리가 다른 동물의 소리인지
    is_fox = [True] * len(record)
    animals = []
    # 다른 동물들 소리 받기
    while True:
        info = input().strip()
        if info == 'what does the fox say?':
            break
        animals.append(list(info.split()))
    # 여우를 제외한 다른 동물들 소리
    other_animals = set()
    for i in range(len(animals)):
        s = animals[i][2]
        other_animals.add(s)
    # 원래 녹음에서 확인
    for i in range(len(record)):
        if record[i] in other_animals:
            is_fox[i] = False
    # 출력
    for i in range(len(record)):
        if is_fox[i]:
            print(record[i], end=' ')
    print()
