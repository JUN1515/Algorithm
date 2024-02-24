import sys
input = sys.stdin.readline

# 세그먼트 트리 생성 및 초기화
def min_init(start, end, index):
    # 해당 구간이 리프노드라면,
    if start == end:
        min_tree[index] = data[start]
        return min_tree[index]

    # 리프노드가 아니라면 리프노드가 될 때까지 두 개의 서브트리로 나눈다
    mid = (start + end) // 2
    min_tree[index] = min(min_init(start, mid, index * 2), min_init(mid + 1, end, index * 2 +1))
    return min_tree[index]


def max_init(start, end, index):
    if start == end:
        max_tree[index] = data[start]
        return max_tree[index]

    mid = (start + end) // 2
    max_tree[index] = max(max_init(start, mid, index * 2), max_init(mid + 1, end, index * 2 +1))
    return max_tree[index]


def min_find(start, end, index, left, right):
    if end < left or right < start:         # 범위를 완전히 벗어난 경우
        return INF

    if left <= start and end <= right:      # 범위 안에 있는 경우(left, right 사이에 start, end가 있는 경우)
        return min_tree[index]

    mid = (start + end) // 2
    return min(min_find(start, mid, index * 2, left, right), min_find(mid + 1, end, index * 2 + 1, left, right))


def max_find(start, end, index, left, right):
    if end < left or right < start:  # 범위를 완전히 벗어난 경우
        return 0

    if left <= start and end <= right:  # 범위 안에 있는 경우(left, right 사이에 start, end가 있는 경우)
        return max_tree[index]

    mid = (start + end) // 2
    return max(max_find(start, mid, index * 2, left, right), max_find(mid + 1, end, index * 2 + 1, left, right))


INF = int(1e9 + 1)
N, M = map(int, input().strip().split())
data = [0] + [int(input()) for _ in range(N)]
min_tree = [0] * (N * 4)
max_tree = [0] * (N * 4)

min_init(1, N, 1)   # 최솟값 트리 생성
max_init(1, N, 1)   # 최댓값 트리 생성

for _ in range(M):
    a, b = map(int, input().strip().split())
    print(min_find(1, N, 1, a, b), max_find(1, N, 1, a, b))