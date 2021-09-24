import sys
input = sys.stdin.readline

N = int(input())  # 회의의 수 / 100,000
timetable = [list(map(int, input().split())) for _ in range(N)]
timetable.sort(key=lambda x:(x[1], x[0]))

answer = 0
i = 0
for st, ed in timetable:
    if i <= st:
        answer += 1
        i = ed
print(answer)
