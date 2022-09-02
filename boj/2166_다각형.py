import sys


def main():
    input = sys.stdin.readline
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    for i in range(N - 1):
        answer += arr[i][0] * arr[i + 1][1]
        answer -= arr[i][1] * arr[i + 1][0]
    # 마지막 항은 첫 항과 묶어 계산
    answer += arr[N - 1][0] * arr[0][1]
    answer -= arr[N - 1][1] * arr[0][0]
    answer = abs(round(answer / 2, 1))
    print(answer)


if __name__ == '__main__':
    main()
