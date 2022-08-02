import sys


def get_cnt(check_num: int, nums: list):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < check_num:
            left = mid + 1
        elif nums[mid] > check_num:
            right = mid - 1
        else:
            answer = 1
            i = 1
            while (mid - i) >= 0:
                if nums[mid - i] == check_num:
                    answer += 1
                else:
                    break
                i += 1
            j = 1
            while (mid + j) < len(nums):
                if nums[mid + j] == check_num:
                    answer += 1
                else:
                    break
                j += 1
            return answer
    return 0


def main():
    N = int(sys.stdin.readline().rstrip())
    nums = sorted(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline().rstrip())
    check_nums = list(map(int, sys.stdin.readline().split()))
    cnt_dict = {}
    answer = []
    for check_num in check_nums:
        if cnt_dict.get(check_num, 0) == 0:
            cnt_value = get_cnt(check_num, nums)
            cnt_dict[check_num] = cnt_value
            answer.append(cnt_value)
        else:
            answer.append(cnt_dict[check_num])
    print(*answer)


if __name__ == '__main__':
    main()
