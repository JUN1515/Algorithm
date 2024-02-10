# refer https://www.acmicpc.net/source/54252298
import sys
input = sys.stdin.readline

def solution():

    def prime_numbers(num):
        numbers = [1] * (num + 1)

        for i in range(2, int(num**(1/2)) + 1):
            if numbers[i]:    # i가 소수인 경우
                for j in range(2 * i, num + 1, i):
                    numbers[j] = 0

        return [i for i in range(2, num + 1) if numbers[i]]

    N = int(input())

    if N == 1:
        print(0)
    else:
        primes = prime_numbers(N)

        a = iter(primes)
        partial_sum = 0     # 부분합
        result = 0

        for b in primes:
            partial_sum += b

            while partial_sum > N:          # 만일 부분합이 N보다 크다면,
                partial_sum -= next(a)      # 부분합 중 가장 작은 소수 제거

            if partial_sum == N:
                result += 1

        print(result)


solution()