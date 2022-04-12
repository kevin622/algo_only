# O(n^2)
import random

arr = [random.randint(0, 100) for _ in range(10)]
print(f'before: {arr}')


def selection_sort(k):
    for i in range(k):
        min_idx = i
        for j in range(i, len(arr), 1):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


selection_sort(len(arr))
print(f'after: {arr}')
