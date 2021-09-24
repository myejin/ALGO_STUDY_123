import sys
input = sys.stdin.readline
# 활동 선택 문제 -> 종료시간을 기준으로 정렬
n = int(input())
meeting = []
for _ in range(n):
    meeting.append(tuple(map(int, input().split())))

# 끝나는 시간이 똑같을 경우 시작 시간이 빠를 것을 선택할 수 있도록
# (2,2) (1,2) 일때 (1,2) (2,2) 일 경우가 될 수 있기 때문에
# key에 튜플로 여러 인자를 주면 인자 순서대로 정렬

meeting.sort(key=lambda x: (x[1], x[0]))

answer = 1
end_time = meeting[0][1]
for i in range(1, n):
    if end_time <= meeting[i][0]:
        answer += 1
        end_time = meeting[i][1]

print(answer)
