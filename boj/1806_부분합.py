import sys

input = sys.stdin.readline


def main():
    N, S = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    for i in range(1, N):
        arr[i + 1] += arr[i]

    # 불가능한 경우
    if arr[N] < S:
        print(0)
        return
    left = 0
    right = 1
    min_len = N
    while 0 <= left < right <= N:
        sub_sum = arr[right] - arr[left]
        if sub_sum >= S:
            min_len = min(min_len, right - left)
            left += 1
        else:
            right += 1
    print(min_len)


if __name__ == '__main__':
    main()
