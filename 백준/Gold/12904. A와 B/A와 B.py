def check_A(left_end, T):
    if left_end >= 0:
        for i in range(left_end, -1, -1):
            if T[i] == "A":
                if i != left_end and T[i + 1] == "B":
                    break
                return False
    return True

def check_B(i, s, t, count_B):
    if i < 0:
        return count_B[t - 1] - count_B[i + s] == 0
    return count_B[i] == count_B[t - 1] - count_B[i + s]

def solution():
    S = input()
    T = input()

    S_reverse = S[::-1] + "B"

    sl = len(S)
    tl = len(T)

    count_B = [0] * tl
    if T[0] == "B": count_B[0] = 1
    for i in range(1, tl):
        if T[i] == "B":
            count_B[i] += 1
        count_B[i] += count_B[i - 1]

    answer = 0
    for i in range(tl - sl + 1):
        if T[i:i + sl] == S:
            if not check_B(i - 1, sl, tl, count_B):
                continue

            if check_A(i - 1, T):
                return 1

    for i in range(tl - sl):
        if T[i:i + sl + 1] == S_reverse:
            if not check_B(i - 1, sl + 1, tl, count_B):
                continue
            return 1
    return 0


print(solution())