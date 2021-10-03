'''
Title : 피보나치 수 5
Link : https://www.acmicpc.net/problem/10870
'''

n = int(input())

def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(n))

