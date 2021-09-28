N = int(input())
answer = 0
neg_nums, pos_nums = [], []
one_cnt, zero = 0, False

for _ in range(N):
    n = int(input())
    if n > 1:
        pos_nums.append(n)
    elif n == 1:
        one_cnt += 1
    elif not n:
        zero = True
    else:
        neg_nums.append(n)

if zero and len(neg_nums) % 2:
    neg_nums.append(0)
neg_nums.sort(reverse=True)
pos_nums.sort()

while len(neg_nums) >= 2:
    answer += neg_nums.pop() * neg_nums.pop()
if neg_nums:
    answer += neg_nums[-1]

while len(pos_nums) >= 2:
    answer += pos_nums.pop() * pos_nums.pop()
if pos_nums:
    answer += pos_nums[-1]

answer += one_cnt
print(answer)
