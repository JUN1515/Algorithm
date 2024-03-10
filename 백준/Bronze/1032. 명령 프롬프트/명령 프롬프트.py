import sys
input = sys.stdin.readline

def solution():
    N = int(input())

    arr = []
    for i in range(N):
        file_name = list(input().strip())
        if not arr:
            arr.extend(file_name)
        else:
            for j in range(len(file_name)):
                if arr[j] != file_name[j]:
                    arr[j] = "?"
    print("".join(arr))


solution()