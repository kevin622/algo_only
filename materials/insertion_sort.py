# O(n^2)
import random

arr = [random.randint(0, 100) for _ in range(10)]
print(f'before: {arr}')


def insertion_sort():
    new_arr = [arr[0]]
    for i in range(1, len(arr)):
        for j in range(len(new_arr) - 1, -1, -1):
            if new_arr[j] < arr[i]:
                new_arr = new_arr[:(j + 1)] + [arr[i]] + new_arr[(j + 1):]
                break
            elif j == 0:
                new_arr = [arr[i]] + new_arr
    return new_arr


arr = insertion_sort()
print(f'after: {arr}')
