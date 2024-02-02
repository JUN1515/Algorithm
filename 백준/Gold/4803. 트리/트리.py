import sys
input = sys.stdin.readline

def dfs(G, visited, start):  # G: 인접행렬, visited: 방문 배열, start: 시작위치
    S = [start]
    visited[start] = 1
    v = start

    is_tree = True
    while S:
        for w in G[v]:
            if not visited[w]:    # 방문한 적이 없다면
                S.append(v)
                visited[w] = 1
                v = w
                break

            if visited[w] == 1 and w != S[-1]:     # 방문한 적 있고, 그 이전 경로가 아니라면
                is_tree = False                     # 싸이클 생성된것 -> 트리가 아님

        else:
            # 끝 부분에 도달한 경우, 이전 경로로 돌아가야 함
            # 하지만 싸이클 생성과 구분하기 위해 추가로 1을 더 더해줌
            # 즉 2는 이미 갔던 가지에 해당(싸이클은 아님)
            visited[v] += 1
            v = S.pop()
    return is_tree


def solution(n, m):

    G = [[] for _ in range(n + 1)]  # 인접리스트
    for _ in range(m):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)

    visited = [0] * (n + 1)

    tree_count = 0
    for i in range(1, n + 1):
        if visited[i]: continue     # 이미 집합에 포함되어 있는 경우
        if dfs(G, visited, i):
            tree_count += 1

    if tree_count == 0:
        return "No trees."
    elif tree_count == 1:
        return "There is one tree."
    else:
        return  f'A forest of {tree_count} trees.'


case = 1
while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    ans = solution(n, m)
    print(f'Case {case}: {ans}')
    case += 1