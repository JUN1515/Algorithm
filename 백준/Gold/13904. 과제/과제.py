import sys

input = sys.stdin.readline
N = int(input())

# studys[i] = [d, w]
studys = [list(map(int, input().split())) for _ in range(N)]

# 점수(w)가 큰 순으로 정렬, 점수가 같은 경우 마감일(d)이 큰 순으로 정렬
studys.sort(key=lambda x:(-x[1], -x[0]))

# 날짜 배열 생성, 0으로 초기화
date = [0] * (N + 1)

# 남은 과제
remain_study = N

for d, w in studys:
    # 남은 과제가 없으면 종료
    if remain_study == 0: break

    # 마감일보다 과제종료일이 더 큰 경우 배열 벗어나는 것을 막기 위해
    index = N if d > N else d

    while index != 0:
        if date[index] == 0:    # 만약 index 날짜에 과제하는게 없으면
            date[index] = w     # 해당 날짜의 요소에 점수 저장
            remain_study -= 1   # 남은 과제 -1
            break
        index -= 1              # index 날짜에 과제가 있으면, 그 전날 확인

print(sum(date))                # date에 저장된 점수 더하기