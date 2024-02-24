import sys
input = sys.stdin.readline

def init(start, end, index):
    if start == end:
        tree[index] = data[start]
        return tree[index]

    mid = (start + end) // 2
    tree[index] = (init(start, mid, index * 2) * init(mid + 1, end, index * 2 + 1)) % MOD
    return tree[index]

def interval_mul(start, end, index, left, right):
    if left > end or right < start:
        return 1

    if left <= start and end <= right:
        return tree[index]

    mid = (start + end) // 2
    return interval_mul(start, mid, index * 2, left, right) * interval_mul(mid + 1, end, index * 2 + 1, left, right) % MOD

def update(start, end, index, change_node, diff):
    if change_node < start or end < change_node:
        return

    if start == end:
        tree[index] = diff
        return tree[index]

    mid = (start + end) // 2
    update(start, mid, index * 2, change_node, diff)
    update(mid + 1, end, index * 2 + 1, change_node, diff)
    tree[index] = tree[index * 2] * tree[index * 2 + 1] % MOD
    return tree[index]

MOD = 1000000007
N, M, K = map(int, input().strip().split())
data = [0] + [int(input()) for _ in range(N)]
tree = [0] * (4 * N)

init(1, N, 1)   # 트리 생성성

for _ in range(M + K):
    a, b, c = map(int, input().strip().split())

    if a == 1:
        update(1, N, 1, b, c)
        data[b] = c
    else:
        print(interval_mul(1, N, 1, b, c) % MOD)