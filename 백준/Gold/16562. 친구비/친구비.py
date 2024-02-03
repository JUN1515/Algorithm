import sys
input = sys.stdin.readline

def solution():

    def find_parent(x):
        if parent[x] != x:
            parent[x] = find_parent(parent[x])
        return parent[x]


    def union_parent(x, y, cost):
        if cost[x] > cost[y]:   # y의 친구비가 더 저렴하면
            parent[x] = y       # y를 루트 친구로
        else:
            parent[y] = x       # x가 더 저렴하면, x를 루트 친구로


    N, M, k = map(int, input().split())    # 학생 수, 친구 관계 수, 가지고 있는 돈
    parent = [i for i in range(N + 1)]

    friend_cost = [0] + list(map(int, input().split()))

    for _ in range(M):
        v, w = map(int, input().split())
        a, b = find_parent(v), find_parent(w)
        if a != b:
            union_parent(a, b, friend_cost)

    total_cost = 0
    for i in range(1, N + 1):
        if parent[i] == i:
            total_cost += friend_cost[i]

    if k - total_cost < 0:
        return "Oh no"
    else:
        return total_cost

print(solution())