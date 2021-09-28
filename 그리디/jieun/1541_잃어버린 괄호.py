import sys
input = sys.stdin.readline
formula = input().split('-')
answer = sum(map(int, formula[0].split('+')))
for i in range(1, len(formula)):
    answer -= sum(map(int, formula[i].split('+')))
print(answer)