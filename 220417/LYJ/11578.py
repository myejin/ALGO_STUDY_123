"""
Title : 팀원 모집
Link : https://www.acmicpc.net/problem/11578
"""

from itertools import combinations
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    N, M = MIIS()
    problems = []
    for _ in range(M):
        _, *problem_set = MIIS()
        problems.append(set(problem_set))
    
    ans = -1
    for i in range(1, N + 1):
        for comb in combinations(problems, i):
            if set().union(*comb) == set(range(1, N + 1)):
                ans = i
                break
        else:
            continue
        break
    print(ans)
