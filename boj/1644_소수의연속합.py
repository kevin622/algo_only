import sys


def main():
    N = int(sys.stdin.readline())
    # N=1이면 0 출력하고 함수 종료
    if N == 1:
        print(0)
        return
    # N 이하의 소수 찾기 - 에라토스테네스 체
    primes = [2]
    is_primes = [True] * (N + 1)
    for i in range(4, N + 1, 2):
        is_primes[i] = False
    for i in range(3, N + 1):
        if is_primes[i]:
            primes.append(i)
            for j in range(i ** 2, N + 1, i * 2):
                is_primes[j] = False
    prime_sums = [0]
    for i in range(len(primes)):
        prime_sums.append(prime_sums[i] + primes[i])

    # 투 포인터
    left = 0
    right = 1
    cnt = 0
    while 0 <= left < right < len(prime_sums):
        val = prime_sums[right] - prime_sums[left]
        if val == N:
            cnt += 1
            left += 1
            right += 1
        elif val < N:
            right += 1
        else:
            left += 1
    print(cnt)


if __name__ == '__main__':
    main()
