"""
Tutke : 늑대와 올바른 단어
Link : https://www.acmicpc.net/problem/13022
"""

def check_rule_1(tmp: list) -> bool:
    l = len(tmp)
    if l % 4:
        return False
    else:
        wolf = 'wolf'
        for i in range(4):
            if tmp[(l//4)*i:(l//4)*(i+1)] != [wolf[i]] * (l // 4):
                return False
    return True


def word_check(word: str):
    tmp = []
    for s in word:
        # 2번 규칙에 따라 한 단어 끝남
        # 1번 규칙 맞는지 확인
        if s == 'w' and (tmp and tmp[-1] == 'f'):
            if not check_rule_1(tmp):
                print(0)
                return
            else:
                tmp = [s]
        else:
            tmp.append(s)
    else:
        if not check_rule_1(tmp):
            print(0)
            return
    print(1)
    return


word = input().strip()
word_check(word)
