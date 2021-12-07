import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# 램프들의 행 정보를 저장
lamp_inp = []
for _ in range(N):
    lamp_inp.append(str(input().strip()))
lamp_inp.sort()  # 동일한 정보는 붙어있도록 정렬
K = int(input())

# 동일한 정보 각각의 개수를 카운트
lamps = []
for i in range(N):
    if i == 0:
        lamps.append([lamp_inp[i], 1])
        continue
    if lamp_inp[i] != lamp_inp[i-1]:
        lamps.append([lamp_inp[i], 1])
    else:
        lamps[-1][1] += 1
# 개수가 많은 정보부터 정렬
lamps.sort(key=lambda x : x[1], reverse=True)

for lamp, cnt in lamps:
    # 램프가 모두 켜지는데 필요한 클릭 횟수
    off_cnt = M - lamp.count('1')
    # 램프를 모두 켤 수 있는 경우
    if K >= off_cnt and off_cnt % 2 == K % 2:
        print(cnt)
        break
# 켤 수 있는 램프가 없는 경우
else:
    print(0)


# # defaultdict 활용 (slow)
# from collections import defaultdict

# N, M = map(int, input().split())
# dic = defaultdict(int)
# for _ in range(N):
#     dic[str(input().strip())] += 1
# lamps = sorted(dic.items(), key=lambda x : x[1], reverse=True)
# K = int(input())

# for lamp, cnt in lamps:
#     off_cnt = M - lamp.count('1')
#     if K >= off_cnt and off_cnt % 2 == K % 2:
#         print(cnt)
#         break
# else:
#     print(0)