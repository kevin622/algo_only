import sys

input = sys.stdin.readline


def main():
    N = int(input())
    dis = list(map(int, input().split()))
    cities = list(map(int, input().split()))

    min_price = cities[0]
    answer = 0
    for i in range(N - 1):
        answer += dis[i] * min_price
        if cities[i + 1] < min_price:
            min_price = cities[i + 1]
    sys.stdout.write(str(answer))


if __name__ == '__main__':
    main()
