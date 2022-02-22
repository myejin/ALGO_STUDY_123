import sys
input = sys.stdin.readline

N = int(input())
balls = []
for i in range(N):
    C, S = map(int, input().split())
    balls.append((C, S, i))
# (색상, 크기, 번호) 로 이루어진 배열을 '크기, 색'을 기준으로 정렬
balls.sort(key=lambda x : (x[1], x[0]))

colors = [0] * (N + 1)  # 색상에 따른 크기 누적 값
color_cnt = balls[0][1]  # 색상에 따른 크기 임시로 저장
total_size = 0  # 크기 누적 값
size_cnt = balls[0][1]  # 크기 임시로 저장
result = [0] * N  # 공 번호에 따른 출력 결과 저장

for i in range(1, N):
    C, S, num = balls[i]  # 현재 공 정보
    pC, pS, pnum = balls[i - 1]  # 이전 공 정보
    # 이전 공과 같은 크기
    if S == pS:
        # 크기가 같은 경우 누적하지 않고 임시로 저장
        size_cnt += S
        # 이전 공과 같은 색상
        if C == pC:
            # 색상이 같은 경우 누적하지 않고 임시로 저장
            color_cnt += S
        else:
            colors[pC] += color_cnt
            color_cnt = S
        # 누적된 크기 값에서 동일한 컬러의 누적 값을 빼고 저장
        result[num] = total_size - colors[C]
    else:
        total_size += size_cnt
        size_cnt = S
        colors[pC] += color_cnt
        color_cnt = S
        # 누적된 크기 값에서 동일한 컬러의 누적 값을 빼고 저장
        result[num] = total_size - colors[C]

for i in result:
    print(i)