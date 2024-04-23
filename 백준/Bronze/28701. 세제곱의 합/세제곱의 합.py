N = int(input())
sum_N = 0
sum_tN = 0
for i in range(1, N + 1):
    sum_N += i
    sum_tN += i * i * i
print(sum_N)
print(sum_N * sum_N)
print(sum_tN)