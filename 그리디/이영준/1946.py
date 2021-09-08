"""
Title : 신입 사원
Link : https://www.acmicpc.net/problem/1946
"""

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    grade = [list(map(int, input().split())) for _ in range(n)]
    grade.sort()
    cnt = 1
    # b = min_grade = grade[0][1]
    b = grade[0][1]
    
    for i in range(1, n):
        d = grade[i][1]
        if b > d:
            cnt += 1
            b = d
        # if d < min_grade:
        #     min_grade = d
    
    print(cnt)