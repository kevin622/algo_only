import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]


# merge sort
def merge(left: list, right: list) -> list:
    result = []
    result_size = len(left) + len(right)
    left_idx = 0
    right_idx = 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result


def merge_sort(arr: list) -> list:
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


sorted_arr = merge_sort(arr)
for num in sorted_arr:
    print(num)
