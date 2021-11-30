score = []
for i in range(10):
    score.append(int(input()))

sum_s = 0

for i in range(10):
    if abs(sum_s + score[i] - 100) <= abs(sum_s-100):
        sum_s+=score[i]
    else:
        break

print(sum_s)