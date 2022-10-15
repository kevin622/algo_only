import sys


def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    arr.sort(key=lambda x: x % 10)
    answer = 0
    for num in arr:
        if num == 10:
            answer += 1
        elif num > 10:
            while M > 0:
                num -= 10
                M -= 1
                answer += 1
                if num <= 10:
                    break
            if num == 10:
                answer += 1
    print(answer)


if __name__ == "__main__":
    main()
