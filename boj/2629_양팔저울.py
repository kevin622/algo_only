import sys

input = sys.stdin.readline


def main():
    N = int(input())  # N <= 30
    weights = list(map(int, input().split()))
    M = int(input())  # M <= 7
    arr = list(map(int, input().split()))
    dp = {weights[0]}
    for weight in weights[1:]:
        for num in list(dp):
            dp.add(num + weight)
            dp.add(abs(num - weight))
        dp.add(weight)

    answer = []
    for num in arr:
        if num in dp:
            answer.append('Y')
        else:
            answer.append('N')
    print(*answer)


if __name__ == '__main__':
    main()
