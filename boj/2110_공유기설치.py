import sys


def main():
    N, C = map(int, sys.stdin.readline().split())
    nums = sorted([int(sys.stdin.readline().rstrip()) for _ in range(N)])
    left = 1
    right = nums[N - 1]
    answer = 0
    while left <= right:
        c_cnt = 1
        mid = (left + right) // 2
        left_point = nums[0]
        for i in range(1, N):
            if (nums[i] - left_point) >= mid:
                left_point = nums[i]
                c_cnt += 1

        if c_cnt >= C:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    print(answer)


if __name__ == '__main__':
    main()
