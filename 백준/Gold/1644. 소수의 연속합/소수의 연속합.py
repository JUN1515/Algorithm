import sys
input = sys.stdin.readline

def solution():

    def prime_numbers(num):
        numbers = [1] * (num + 1)

        for i in range(2, int(num**(1/2)) + 1):
            if numbers[i]:    # i가 소수인 경우
                for j in range(2 * i, num + 1, i):
                    numbers[j] = 0

        prime = [0]
        for i in range(2, num + 1):
            if numbers[i]:
                prime.append(i)

        return prime

    N = int(input())

    if N == 1:
        return 0

    else:
        arr = prime_numbers(N)
        prefix_sum = [0] * len(arr)

        a = 0
        count = 0

        for b in range(1, len(arr)):
            prefix_sum[b] = prefix_sum[b - 1] + arr[b]

            while a != b:   # 만일 포인터 a와 b가 같은 위치를 가리키면 종료
                partial_sum = prefix_sum[b] - prefix_sum[a] # 부분합

                # 만일 부분합이 N보다 크다면,
                # 부분합을 줄이기 위해 a의 위치를 오른쪽으로 이동
                if partial_sum > N:
                    a += 1

                # 만일 부분합이 N 보다 작은 경우는 반복문 종료
                # (부분합의 크기를 줄이지 않기 위함)
                else:
                    if partial_sum == N:
                        a += 1
                        count += 1
                    break

        return count


print(solution())