import sys
input = sys.stdin.readline

def solution():
    N = int(input().strip())
    arr = list(map(int, input().strip().split()))
    mul_arr = [0] * N
    add_arr = [0] * N

    for i in range(N):
        val = arr[i]
        while val != 0:
            if val % 2:
                add_arr[i] += 1
                val -= 1
                continue
            val = val // 2
            mul_arr[i] += 1
    result = max(mul_arr) + sum(add_arr)
    print(result)


solution()