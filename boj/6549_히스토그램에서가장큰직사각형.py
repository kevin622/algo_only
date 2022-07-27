import sys


def get_biggest(start: int, end: int, heights: list) -> int:
    if start == end:
        return heights[start]
    mid = (start + end) // 2
    left = mid
    right = mid + 1

    left_biggest = get_biggest(start, left, heights)
    right_biggest = get_biggest(right, end, heights)

    height = min(heights[left], heights[right])
    mid_biggest = height * 2
    while left != start or right != end:
        left_height = -1
        right_height = -1
        if start < left:
            left_height = min(height, heights[left - 1])
        if right < end:
            right_height = min(height, heights[right + 1])
        if left_height > right_height:
            height = left_height
            left -= 1
        else:
            height = right_height
            right += 1
        mid_biggest = max(mid_biggest, height * (right - left + 1))
    return max(left_biggest, right_biggest, mid_biggest)


def main():
    while True:
        nums = sys.stdin.readline().rstrip()
        if nums == '0':
            return
        nums = list(map(int, nums.split()))
        n = nums[0]
        heights = nums[1:]
        print(get_biggest(0, n - 1, heights))


if __name__ == '__main__':
    main()
