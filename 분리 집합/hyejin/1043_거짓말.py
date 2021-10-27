N, M = map(int, input().split())
known_people = set(list(map(int, input().split()))[1:])
parties = [set(list(map(int, input().split()))[1:]) for _ in range(M)]
# print(parties)
chk = [0] * M
for _ in range(M):
    for idx, party in enumerate(parties):
        if known_people & party:
            chk[idx] = 1
            known_people |= party

print(chk.count(0))
