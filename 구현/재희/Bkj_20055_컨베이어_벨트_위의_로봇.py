from collections import deque

def work():
    global K, belt, robots, cnt
    while True:
        # 벨트와 로봇 회전
        belt.rotate(1)
        robots.rotate(1)
        # 마지막에 있는 로봇 내리기
        robots[-1] = 0
        # 벨트 뒤부터 탐색
        for i in range(N - 2, 0, -1):
            # 로봇이 있음, 벨트 내구도 있음, 다음 칸에 로봇 없음
            if robots[i] and belt[i + 1] and not robots[i + 1]:
                # 벨트 내구도 감소
                if belt[i + 1] == 1:
                    K -= 1
                    if not K:
                        return
                belt[i + 1] -= 1
                robots[i] = 0
                # 마지막에 도착하는 로봇은 바로 내림
                if i != N - 2:
                    robots[i + 1] = 1
        # 처음 벨트에 로봇 올리기
        if belt[0]:
            if belt[0] == 1:
                K -= 1
                if not K:
                    return
            belt[0] -= 1
            robots[0] = 1
        # 수행 단계 증가
        cnt += 1


N, K = map(int, input().split())
belt = deque(map(int, input().split()))  # 벨트 내구도
robots = deque([0] * N)  # 로봇 위치

cnt = 1  # 수행 단계
work()

print(cnt)