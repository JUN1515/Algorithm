import sys
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(x, y):
    if x > y:
        parent[x] = y
    else:
        parent[y] = x

T = int(input())
for _ in range(T):

    N = int(input())
    parent = [i for i in range(N)]
    arr = [tuple(map(int, input().split())) for _ in range(N)]

    result = 0

    for i in range(N):
        x1, y1, r1 = arr[i]

        for j in range(i + 1, N):
            x2, y2, r2 = arr[j]

            if ((x1 - x2)**2 + (y1 - y2)**2) <= (r1 + r2)**2:     # 두 점 사이의 거리가 각 두 점의 반지름의 합보다 작은 경우
                if (a := find_parent(i)) == (b := find_parent(j)): continue
                union_parent(a, b)

    for i in range(N):
        if find_parent(i) == i:
            result += 1

    print(result)