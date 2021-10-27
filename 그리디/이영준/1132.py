"""
Title : 합
Link : https://www.acmicpc.net/problem/1132
"""

import sys
input = sys.stdin.readline


n = int(input())

alp_weight = {chr(65 + i): 0 for i in range(10)}
# 1개만 존재하면 0으로 사용 불가능
zero_possible = {chr(65 + i): True for i in range(10)}

# 알파벳 숫자 저장
numbers = []
for _ in range(n):
    # 가중치를 10의 자리수 제곱으로 더해주기
    power = 0
    num = input().strip()
    numbers.append(num)
    while num:
        if len(num) == 1:
            zero_possible[num] = False
        alp_weight[num[-1]] += 10 ** power
        power += 1
        num = num[:-1]

# 각각 알파벳 가중치별 정렬, 대응할 숫자 확인
alp_weight_list = sorted(alp_weight.items(), key=lambda x: x[1], reverse=True)
alp_num = {chr(65 + i): 0 for i in range(10)}
num_alp = {i: '' for i in range(10)}
idx = 9
for alp, w in alp_weight_list:
    if not w:
        break
    alp_num[alp] = idx
    num_alp[idx] = alp
    idx -= 1

# 0까지 모두 사용한 경우, 0으로 배치 가능한지
if num_alp[0]:
    # 0에 할당한 알파벳이 0으로 사용 못할 때
    if not zero_possible[num_alp[0]]:
        # 0부터 9까지 탐색하며 0으로 사용하가능한 알파벳 확인
        for i in range(1, 10):
            if zero_possible[num_alp[i]]:
                tmp_alp, tmp_num = num_alp[i], i
                break
        # tmp_num부터 1까지 내려가며 1 더 작은수에 할당된 알파벳 하나씩 변환
        for i in range(tmp_num, 0, -1):
            alp_now = num_alp[i - 1]
            num_alp[i] = alp_now
            alp_num[alp_now] = i
        # num_alp는 변경해줄 필요 없음
        alp_num[tmp_alp] = 0

# 각각을 숫자로 변환
sum_convert_numbers = 0
for num in numbers:
    convert_num = 0
    for alp in num:
        convert_num *= 10
        convert_num += alp_num[alp]
    sum_convert_numbers += convert_num

print(sum_convert_numbers)
