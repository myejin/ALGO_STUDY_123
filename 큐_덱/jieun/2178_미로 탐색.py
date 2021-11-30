import sys
input = sys.stdin.readlines

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
inf = 100000
visited = []