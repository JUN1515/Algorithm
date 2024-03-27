import sys
input = sys.stdin.readline

def solution():
    N = int(input().strip())
    for _ in range(N):
        S = input().strip()
        if 6 <= len(S) <= 9: print("yes");
        else: print("no")            

solution()