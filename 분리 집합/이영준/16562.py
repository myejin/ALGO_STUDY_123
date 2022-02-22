"""
Title : 친구비
Link : https://www.acmicpc.net/problem/16562
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def solution():
    """Main solution function
    """
    N, M, K = MIIS()
    friend_prices = list(MIIS())
    parents = [i for i in range(N + 1)]
    for _ in range(M):
        v, w = MIIS()
        v, w = find_parent(v, parents), find_parent(w, parents)
        parents = union_parent(v, w, parents)

    new_parents = {i: 0 for i in range(1, N + 1)}
    for i in range(1, N + 1):
        parent, min_price_value = calc_min_friend_price(i, friend_prices, parents)
        if not new_parents[parent] or new_parents[parent] > min_price_value:
            new_parents[parent] = min_price_value
    friend_prices_count = sum(new_parents.values())
    print(friend_prices_count if friend_prices_count <= K else 'Oh no')
    return None


def find_parent(x: int, parents: list) -> int:
    """find x's parent

    Parameters
    ----------
    x : int
    parents : list

    Returns
    -------
    int
        parent of x
    """
    while x != parents[x]:
        x = parents[x]
    return x


def union_parent(x: int, y: int, parents: list) -> list:
    """union two points x and y

    Parameters
    ----------
    x : int
    y : int
    parents : list

    Returns
    -------
    list
    """
    if x > y:
        parents[x] = y
    else:
        parents[y] = x
    return parents


def calc_min_friend_price(x: int, friend_prices: list, parents: list) -> tuple:
    """calculate minimun friend price
    from x to parent of x

    Parameters
    ----------
    x : int
    friend_prices : list
    parents : list

    Returns
    -------
    tuple
        parent of x & min friend price
    """
    min_friend_price = friend_prices[x - 1]
    while x != parents[x]:
        x = parents[x]
        if min_friend_price > friend_prices[x - 1]:
            min_friend_price = friend_prices[x - 1]
    return x, min_friend_price


solution()


'''
Counter Exmaples
5 4 100
1 1 1 1 1
1 5
2 4
4 3
5 4

5 3 20
10 20 20 10 30
1 3
2 4
5 4
'''
