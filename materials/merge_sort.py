# O(n * log(n))
import random

arr = [random.randint(0, 100) for _ in range(10)]
print(f'before: {arr}')


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


arr = merge_sort(arr)
print(f'after: {arr}')
