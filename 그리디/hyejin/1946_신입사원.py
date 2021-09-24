import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())  # 지원자 수 / 100,000
    ranks = [list(map(int, input().split())) for _ in range(N)]
    ranks.sort(key=lambda x:-x[0])
    highest_rank = 1
    exclude = 0
    
    for i in range(N - 1):
        if ranks[i][1] == highest_rank:
            highest_rank += 1
            continue
        for j in range(i + 1, N):
            if ranks[i][1] > ranks[j][1]:
                exclude += 1
                break

    print(N - exclude)
