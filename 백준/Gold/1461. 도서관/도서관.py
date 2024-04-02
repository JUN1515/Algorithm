import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().strip().split())
    books = map(int, input().strip().split())
    left = []
    right = []
    for book in books:
        if book < 0:
            left.append(abs(book))
        else:
            right.append(book)


    answer = 0

    left.sort(reverse=True)
    for i in range(len(left)//M):
        answer += (left[i * M] * 2)
    if l := len(left) % M:
        answer += (left[-l] * 2)

    right.sort(reverse=True)
    for i in range(len(right) // M):
        answer += (right[i * M] * 2)
    if r := len(right) % M:
        answer += (right[-r] * 2)

    if len(right) and len(left):
        answer -= left[0] if left[0] > right[0] else right[0]
    elif len(left):
        answer -= left[0]
    elif len(right):
        answer -= right[0]
    print(answer)


solution()