import sys
input = sys.stdin.readline

N, M = map(int, input().split())    # 사람 수, 파티 수
know_persons = set(input().split()[1:])
parties = [set(input().split()[1:]) for _ in range(M)]

for _ in range(M):
    for party in parties:
        if party & know_persons:
            know_persons |= party

ans = M
for party in parties:
    if party & know_persons:
        ans -= 1
print(ans)