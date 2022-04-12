# O(n^2)
import random

arr = [random.randint(0, 100) for _ in range(10)]
print(f'before: {arr}')


def bubble_sort():
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


bubble_sort()
print(f'after: {arr}')
