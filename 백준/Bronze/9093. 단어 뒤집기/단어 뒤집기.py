import sys;
input = sys.stdin.readline

def solution(s):
    temp = ""
    left = 0
    for right in range(len(s)):
        if s[right] == " ":
            temp += s[left: right][::-1] + " "
            left = right + 1
    else:
        temp += s[left: right + 1][::-1]
    print(temp)

T = int(input())
for _ in range(T):
    S = input().strip()
    solution(S)