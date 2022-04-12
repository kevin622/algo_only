import sys

input = sys.stdin.readline
N = int(input())
arr = [int(input()) for _ in range(N)]


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


quick_sort(arr, 0, N - 1)

for num in arr:
    print(num)
