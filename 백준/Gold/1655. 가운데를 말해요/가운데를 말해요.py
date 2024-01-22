import sys
from heapq import *

input = sys.stdin.readline
N = int(input())

left = [-int(input())]      # 중간 값과 같거나 작은 수, 최대힙
right = []                  # 중간 값보다 큰 수, 최소힙

ans = [str(-left[0])]       # 결과 값 (한번에 출력하기 위한 배열)
count = 1                   # 입력된 수의 갯수

if N > 1:
    for i in range(N-1):
        num = int(input())

        if -left[0] >= num:         # 입력된 수가 중간 값보다 같거나 작은 경우
            heappush(left, -num)    # 일단 작은 쪽(left) 배열에 넣고
            if count % 2 == 1:      # 입력된 수가 홀수인 경우 (len(left) > len(right))
                heappush(right, -heappop(left))     # left 배열의 가장 큰 수를 right 배열로 이동

        elif -left[0] < num:        # 입력된 수가 중간 값보다 더 큰 경우

            heappush(right, num)
            if count % 2 == 0:
                heappush(left, -heappop(right))

        ans.append(str(-left[0]))
        count += 1
print('\n'.join(ans))