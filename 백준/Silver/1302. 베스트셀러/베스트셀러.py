import sys
input = sys.stdin.readline

def solution():
    N = int(input().strip())
    books = {}

    for _ in range(N):
        book = input().strip()
        books[book] = books.get(book, 0) + 1

    arr = sorted(list(books))
    answer = arr[0]
    for i in range(len(arr)):
        if books[answer] < books[arr[i]]:
            answer = arr[i]
    print(answer)


solution()