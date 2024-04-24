T = int(input())
answer = ""
for _ in range(T):
    answer += str(min(map(int, input().split()))) + "\n"
print(answer, end="")