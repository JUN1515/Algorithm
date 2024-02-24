import sys
input = sys.stdin.readline

# 세그먼트 트리 생성 및 초기화
def init(start, end, index):
    # 해당 구간이 리프노드라면,
    if start == end:
        tree[index] = data[start]
        return tree[index]

    # 리프노드가 아니라면 리프노드가 될 때까지 두 개의 서브트리로 나눈다
    mid = (start + end) // 2
    tree[index] = init(start, mid, index * 2) + init(mid + 1, end, index * 2 + 1)
    return tree[index]

# 구간 합 구하는 함수
# start, end: 시작 인덱스, 끝 인덱스 / index: tree의 인덱스 / left, right : 구간 합을 구하고 싶은 범위
def interval_sum(start, end, index, left, right):
    # 범위 밖에 있는 경우
    if left > end or right < start:
        return 0

    # 범위 안에 있는 경우
    if left <= start and end <= right:
        return tree[index]

    # 그렇제 않다면 두 부분으로 나누어 합을 구하기
    mid = (start + end) // 2
    # start와 end를 변경하면서 구간에 해당하는 부분은 모두 더해준다고 생각하면 됨
    return interval_sum(start, mid, index * 2, left, right) + interval_sum(mid + 1, end, index * 2 + 1, left, right)


# 특정 원소의 값을 수정하는 함수
# start, end : 시작 인덱스, 끝 인덱스
# index : tree의 인덱스
# change_node : 수정하고자 하는 노드
# change_val : 수정할 값 (기존 값과의 차이)
def update(start, end, index, change_node, change_val):
    # 범위 밖에 있는 경우
    if change_node < start or end < change_node:
        return

    # 범위 안에 있으면 트리를 내려가면서 다른 원소도 갱신
    tree[index] += change_val
    if start == end:
        return

    mid = (start + end) // 2
    update(start, mid, index * 2, change_node, change_val)
    update(mid + 1, end, index * 2 + 1, change_node, change_val)


N, M, K = map(int, input().strip().split())
data = [0] + [int(input()) for _ in range(N)]
tree = [0] * (4 * N)

init(1, N, 1)   # 트리 생성성

for _ in range(M + K):
    a, b, c = map(int, input().strip().split())

    if a == 1:  # b번째 수를 c로 변경
        val = c - data[b]
        data[b] = c                 # data 업데이트
        update(1, N, 1, b, val)     # tree 업데이트
    else:       # b번째 수부터 c번째 수까지의 합을 출력
        print(interval_sum(1, N, 1, b, c))