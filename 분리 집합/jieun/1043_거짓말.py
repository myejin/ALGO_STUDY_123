import sys
input = sys.stdin.readline


def find_p(x):
    if p[x] != x:
        p[x] = find_p(p[x])
        return p[x]
    else:
        return x


n, m = map(int, input().split())
know_true = list(map(int, input().split()))
know_true = know_true[1:]
p = [i for i in range(n+1)]
parties = []
for _ in range(m):
    persons = list(map(int, input().split()))
    parties.append(persons)
    for i in range(1, persons[0]+1):
        for j in range(i + 1, persons[0]+1):
            p1 = find_p(persons[i])
            p2 = find_p(persons[j])
            p[p1] = p2

if know_true:
    ans = 0
    know_true_p = set(find_p(x) for x in know_true)
    for party in parties:
        for i in range(1, party[0]+1):
            if find_p(party[i]) in know_true_p:
                break
        else:
            ans += 1
    print(ans)

else:
    print(len(parties))
