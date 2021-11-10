"""
Title : 5의 수난
Link : https://www.acmicpc.net/problem/23037
"""

five_num = tuple(map(int, input().strip()))
result = 0
for num in five_num:
    result += num * num * num * num * num
print(result)
