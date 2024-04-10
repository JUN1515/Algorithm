import sys
input = sys.stdin.readline

def solution(T, word):
    count = 0
    stack = 0

    for ch in word:
        if ch == '{':
            stack += 1

        else:
            if stack == 0:
                count += 1
                stack += 1
            else:
                stack -= 1
    count += stack // 2
    print(f'{T}. {count}')


T = 1
while (word := input().strip())[0] != '-':
    solution(T, word)
    T += 1