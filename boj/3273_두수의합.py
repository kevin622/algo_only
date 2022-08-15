import sys

input = sys.stdin.readline


def main():
    n = int(input())
    arr = sorted(map(int, input().split()))
    x = int(input())
    if n == 1:
        print(0)
        return
    answer = 0
    start = 0
    end = n - 1
    while start < end:
        val = arr[start] + arr[end]
        if val == x:
            answer += 1
            start += 1
            end -= 1
        elif val < x:
            start += 1
        elif val > x:
            end -= 1
    print(answer)


if __name__ == '__main__':
    main()
