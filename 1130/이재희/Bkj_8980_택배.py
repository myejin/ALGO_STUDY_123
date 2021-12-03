import sys, heapq
input = sys.stdin.readline

N, C = map(int, input().split())
M = int(input())
boxes = [list(map(int, input().split())) for _ in range(M)]
boxes.sort(key = lambda x : (x[0], x[1]))
truck_load = 0  # 트럭 적재량
total_box = 0

# 각 마을로 배송 예정인 박스 수
box_of_town = [0] * (N+1)

# 실어 놓은 박스 중 배송지가 먼 순서대로 힙 구성
max_heap = []

last_town = 0
for now_town, end_town, box in boxes:
    # 중간에 뛰어넘은 마을이 있을 경우 박스 수 합산
    if last_town < (now_town - 1):
        total_box += sum(box_of_town[last_town:now_town])
        truck_load -= sum(box_of_town[last_town:now_town])
    total_box += box_of_town[now_town]
    truck_load -= box_of_town[now_town]
    box_of_town[now_town] = 0
    # 남은 적재량 보다 실을 박스가 많은 경우
    if box > (C - truck_load):
        remain_box = box - (C - truck_load)
        box_of_town[end_town] += (C - truck_load)
        truck_load = C
        # 실려 있는 박스의 배송지가 실을 박스의 배송지보다 먼 경우
        while end_town < -max_heap[0]:
            # 실려 있는 박스가 실을 박스보다 많을 경우
            if remain_box < box_of_town[-max_heap[0]]:
                box_of_town[end_town] += remain_box
                box_of_town[-max_heap[0]] -= remain_box
                break
            max_town = -heapq.heappop(max_heap)
            box_of_town[end_town] += box_of_town[max_town]
            remain_box -= box_of_town[max_town]
            box_of_town[max_town] = 0
    else:
        truck_load += box
        box_of_town[end_town] += box
    heapq.heappush(max_heap, -end_town)
    last_town = now_town

# 남아 있는 박스 합산
total_box += sum(box_of_town[now_town:])

print(total_box)