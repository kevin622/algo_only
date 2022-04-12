# O(n*log(n)) but O(n^2) at worse case
import random

arr = [random.randint(0, 1000) for _ in range(1000)]

print(f'before: {arr}')


def quick_sort(arr: list, begin: int, end: int) -> None:
    if begin < end:
        P = partition(arr, begin, end)
        quick_sort(arr, begin, P - 1)
        quick_sort(arr, P + 1, end)


def partition(arr: list, begin: int, end: int) -> int:
    pivot = (begin + end) // 2
    L = begin
    R = end
    while L < R:
        while arr[L] < arr[pivot] and L < R:
            L += 1
        while arr[pivot] <= arr[R] and L < R:
            R -= 1
        if L < R:
            if L == pivot:
                pivot = R
            arr[L], arr[R] = arr[R], arr[L]
    arr[pivot], arr[R] = arr[R], arr[pivot]
    return R


quick_sort(arr, 0, len(arr) - 1)
print(f'after: {arr}')
