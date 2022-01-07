import sys

input = lambda : sys.stdin.readline()

def init(start, end, node):
    global seq, segment_tree
    if start == end:
        segment_tree[node] = seq[start]
        return(seq[start])
    mid = (start + end) // 2
    init(start, mid, node * 2)
    init(mid + 1, end, node * 2 + 1)
    segment_tree[node] = segment_tree[node * 2] + segment_tree[node * 2 + 1]

def partial_sum(start, end, node, left, right):
    global segment_tree
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return segment_tree[node]
    mid = (start + end) // 2
    return partial_sum(start, mid, node * 2, left, right) + partial_sum(mid + 1, end, node * 2 + 1, left, right)


n, m = map(int, input().split())
seq = [0] + list(map(int, input().split()))
segment_tree = [0] * (4 * n)
init(1, n, 1)

for _ in range(m):
    a, b= map(int, input().split())
    s = partial_sum(1, n, 1, a, b)
    print(s)