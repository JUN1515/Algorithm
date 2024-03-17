import sys
input = sys.stdin.readline

def count_num(arrs):
    count = 0
    for arr in arrs:
        for elm in arr.split('X'):
            if len(elm) >= 2:
                count += 1
    return count

def solution():
    row = col = 0

    N = int(input())
    arr = [input().strip() for _ in range(N)]
    r_arr = [''.join(lst) for lst in list(zip(*arr))]

    row = count_num(arr)
    col = count_num(r_arr)
    print(row, col)


solution()