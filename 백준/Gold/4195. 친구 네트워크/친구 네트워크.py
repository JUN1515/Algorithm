import sys
input = sys.stdin.readline

def friend_index(friend_name):          # 친구 이름을 숫자로 관리하기 위함.
    global friend_num, parent, index
    if friend_num.get(friend_name, 0) == 0:
        friend_num[friend_name] = index
        parent.append(-1)
        index += 1


def find_parent(x):
    if parent[x] < 0:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(x, y):
    if parent[x] > parent[y]:
        parent[y] += parent[x]
        parent[x] = y
        return parent[y]
    else:
        parent[x] += parent[y]
        parent[y] = x
        return parent[x]


T = int(input())

for _ in range(T):
    F = int(input())        # 친구관계의 수
    friend_num = {}
    parent = [-1]           # 요소는 음의 값이 루트 노드임을 나타내면서도, 해당 트리에 포함된 리프의 개수의 음의 값을 의미

    index = 1
    for _ in range(F):
        f1, f2 = input().split()

        # friend_num 배열에 친구 이름이 있는지 확인
        friend_index(f1)
        friend_index(f2)

        a, b = friend_num[f1], friend_num[f2]
        pa, pb = find_parent(a), find_parent(b)
        if pa == pb:
            print(-parent[pa])
        else:
            print(-union_parent(pa, pb))