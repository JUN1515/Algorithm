import sys;
from itertools import zip_longest
input = sys.stdin.readline

def solution():
    arr = []
    for i in range(5):
        arr.append(list(input().strip()))

    b = list(zip_longest(*arr, fillvalue=""))


    for i in range(len(b)):
        print("".join(b[i]), end="")
    print()


solution()