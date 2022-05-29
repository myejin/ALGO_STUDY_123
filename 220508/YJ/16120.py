"""
Title : PPAP
Link : https://www.acmicpc.net/problem/16120
"""

import sys
input = sys.stdin.readline


if __name__ == "__main__":
    ppap = input().strip() + " "
    p_count = 0
    for idx, s in enumerate(ppap):
        if s == "P":
            p_count += 1
            continue
        if s == "A" and ppap[idx + 1] == "P" and p_count >= 2:
            p_count -= 2
        elif s != " ":
            print("NP")
            break
    else:
        if p_count == 1:
            print("PPAP")
        else:
            print("NP")

'''
PPPPAAP
'''
