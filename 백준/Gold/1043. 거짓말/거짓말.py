import sys
input = sys.stdin.readline


def find_parent(x):
    if parent[x] < 0:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(x, y):
    if parent[x] > parent[y]:
        parent[x] = y
    else:
        if parent[x] == parent[y]:
            parent[x] -= 1
        parent[y] = x


N, M = map(int, input().split())    # 사람 수, 파티 수
parent = [-1] * (N + 1)

# know_persons
k_n, *know_persons = list(map(int, input().split()))
if k_n > 1:
    for i in range(1, k_n):
        parent[know_persons[i]] = know_persons[0]

ans = M
if k_n != 0:
    parent[know_persons[0]] = -50  # 항상 루트 노드가 되게 하기 위해

    arrs = [list(map(int, input().split())) for _ in range(M)]
    
    for arr in arrs:        # 분리 집합
        n, *persons = arr

        if n != 1:
            x = find_parent(persons[0])
            for i in range(1, n):
                if (y := find_parent(persons[i])) != x:
                    union_parent(x, y)
                    x = y

    for arr in arrs:        
        n, *persons = arr

        for person in persons:
            if find_parent(person) == know_persons[0]:
                ans -= 1
                break
print(ans)