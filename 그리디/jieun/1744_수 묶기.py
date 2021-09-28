# 양수 x 양수, 음수 x 음수
import sys
input = sys.stdin.readline
n = int(input())
gt_arr = []
lt_arr = []
answer = 0
for _ in range(n):
    a = int(input())
    if a == 1:
        answer += 1
    elif a > 1:
        gt_arr.append(a)
    else:
        lt_arr.append(a)

gt_arr.sort(reverse=True)
lt_arr.sort()

if len(gt_arr) % 2 :
    for idx in range(0, len(gt_arr)-1, 2):
        answer += gt_arr[idx]*gt_arr[idx+1]
    answer += gt_arr[-1]
else:
    for idx in range(0, len(gt_arr), 2):
        answer += gt_arr[idx]*gt_arr[idx+1]

if len(lt_arr) % 2:
    for idx in range(0, len(lt_arr)-1, 2):
        answer += lt_arr[idx]*lt_arr[idx+1]
    answer += lt_arr[-1]
else:
    for idx in range(0, len(lt_arr), 2):
        answer += lt_arr[idx] * lt_arr[idx+1]

print(answer)