import sys

input = sys.stdin.readline


def main():
    N = int(input())
    arr = sorted(map(int, input().split()))
    if arr[0] > 0:
        print(arr[0], arr[1])
        return
    if arr[N - 1] < 0:
        print(arr[N - 2], arr[N - 1])
        return
    left = 0
    right: int = N - 1
    min_sum = int(1e10)
    answer: list = [0, 0]
    while left < right:
        val = arr[left] + arr[right]
        if val == 0:
            answer = [arr[left], arr[right]]
            break
        if abs(val) < min_sum:
            min_sum = abs(val)
            answer = [arr[left], arr[right]]
        if val < 0:
            left += 1
        else:
            right -= 1
    print(*answer)


if __name__ == '__main__':
    main()
