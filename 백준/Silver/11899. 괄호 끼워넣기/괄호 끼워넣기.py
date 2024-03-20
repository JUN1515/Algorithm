def solution():
    S = input()

    cnt = 0
    left = 0

    for ch in S:
        if ch == ')':
            if left == 0:
                cnt += 1
            else:
                left -= 1
        else:
            left += 1
    cnt += left
    print(cnt)


solution()