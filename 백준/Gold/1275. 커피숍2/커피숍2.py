import sys
input = sys.stdin.readline

def init(start, end, index):
    if start == end:
        tree[index] = data[start]
        return tree[index]

    mid = (start + end) // 2
    tree[index] = init(start, mid, index * 2) + init(mid + 1, end, index * 2 + 1)
    return tree[index]

def interval_sum(start, end, index, left, right):
    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return tree[index]

    mid = (start + end) // 2
    return interval_sum(start, mid, index * 2, left, right) + interval_sum(mid + 1, end, index * 2 + 1, left, right)

def update(start, end, index, change_node, change_val):
    if change_node < start or end < change_node:
        return

    tree[index] += change_val
    if start == end:
        return

    mid = (start + end) // 2
    update(start, mid, index * 2, change_node, change_val)
    update(mid + 1, end, index * 2 + 1, change_node, change_val)


N, Q = map(int, input().strip().split())
data = [0] + list(map(int, input().strip().split()))
tree = [0] * (4 * N)

init(1, N, 1)   # 트리 생성성

for _ in range(Q):
    x, y, a, b = map(int, input().strip().split())
    if x > y:
        x, y = y, x
    print(interval_sum(1, N, 1, x, y))
    val = b - data[a]
    update(1, N, 1, a, val)     # tree 업데이트
    data[a] = b                 # data 업데이트