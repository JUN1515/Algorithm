import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    arr = [list(map(int, input().strip().split())) for _ in range(N)]
    arr.sort(key = lambda x: -x[2])
    
    answer = []
    dic = {}
    count = 0
    for a, b, s in arr:
        if dic.get(a, 0) == 2: continue
        answer.append((a, b))
        dic[a] = dic.get(a, 0) + 1
        count += 1
        if count == 3:
            break
    for i in range(3):
        print(*answer[i])


solution()