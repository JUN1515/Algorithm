import sys
input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] < 0:
        return x
    parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, x, y):
    if parent[x] > parent[y]:
        parent[x] = y
    else:
        if parent[x] == parent[y]:
            parent[x] -= 1
        parent[y] = x


def solution(n, m):
    parent = [-1] * (n + 1)
    arr = [list(map(int, input().split())) for _ in range(m)]

    # 서로소 알고리즘
    for i in range(m):
        a, b = arr[i]
        x, y = find_parent(parent, a), find_parent(parent, b)
        if x != y:
            union_parent(parent, x, y)

    r_nodes = {} # key: 루트 노드, value: [집합에 속한 노드 수, 간선 수]

    # 집합의 개수 확인(루트 노드의 개수로 확인)
    for i in range(1, n + 1):
        key = find_parent(parent, i)
        r_nodes[key] = r_nodes.get(key, 0) + 1

    # 집합의 간선 수 확인(루트 노드로 집합 구분)
    for i in range(m):
        key = find_parent(parent, arr[i][0])
        r_nodes[key] -= 1

    count = 0

    # 트리를 확인, value값이 1이면 tree
    for val in r_nodes.values():
        if val == 1:
            count += 1

    if count == 0:
        return "No trees."
    elif count == 1:
        return "There is one tree."
    else:
        return  f'A forest of {count} trees.'

case = 1
while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    ans = solution(n, m)
    print(f'Case {case}: {ans}')
    case += 1