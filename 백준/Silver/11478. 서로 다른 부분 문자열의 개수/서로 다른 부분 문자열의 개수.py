import sys
sys.setrecursionlimit(2000)
def func(n, string):
    if n == N:
        answer.add(string)
        return

    func(n + 1, string + S[n])
    if string == "":
        func(n + 1, string)
    else:
        answer.add(string)
        return

S = input().strip()
N = len(S)

answer = set()
func(0, "")

print(len(answer) - 1)