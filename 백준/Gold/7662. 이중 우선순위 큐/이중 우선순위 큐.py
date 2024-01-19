import sys
from heapq import *

def del_number(arr, d):
    global numbers

    while True:
        dn = heappop(arr) * d
        if numbers[dn] != 0:
            numbers[dn] -= 1
            return dn


input = sys.stdin.readline
T = int(input())

for _ in range(T):
    k = int(input())    # Q에 적용할 연산의 개수

    min_heap = []       # 오름차순 -> 'D -1'일 때 최솟값 제거
    max_heap = []       # 내림차순 -> 'D 1'일 때 최댓값 제거
    heapify(min_heap)
    heapify(max_heap)

    numbers = {}        # key: Q에 있는 정수, value: 정수의 갯수
    count = 0           # Q에 있는 정수의 갯수
    for _ in range(k):
        comd, num = input().split()
        if comd == 'I':
            num = int(num)
            heappush(min_heap, num)
            heappush(max_heap, -num)

            numbers[num] = numbers.get(num, 0) + 1
            count += 1

        elif comd == 'D':
            if not count: continue      # Q가 비어있으면 연산 무시
            if num == '1':              # 최댓값 제거
                del_number(max_heap, -1)
            elif num == '-1':           # 최솟값 제거
                del_number(min_heap, 1)

            count -= 1
            if not count:
                min_heap, max_heap = [], []

    if count == 0:
        print('EMPTY')
    elif count == 1:
        result = del_number(min_heap, 1)
        print(result, result)
    else:
        print(del_number(max_heap, -1), del_number(min_heap, 1))