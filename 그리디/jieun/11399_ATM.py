n = int(input())
atm = list(map(int, input().split()))
atm.sort()

sum_p = acc = 0

for person in atm:
    sum_p += acc + person
    acc += person

print(sum_p)