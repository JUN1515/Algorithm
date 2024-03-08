def solution():
    arr = list(input())

    if "0" not in arr:
        return -1

    sum_N = 0
    for i in arr:
        sum_N += int(i)
    if sum_N % 3:
        return -1
    else:
        return int("".join(sorted(arr, reverse=True)))


print(solution())