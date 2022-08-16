import sys

input = sys.stdin.readline


def main():
    N = int(input())
    arr = list(map(int, input().split()))
    vec = [int(-1e10)]
    indices = []
    for num in arr:
        if vec[-1] < num:
            vec.append(num)
            indices.append(len(vec) - 1)
        else:
            # 이분탐색
            left = 0
            right = len(vec) - 1
            while left <= right:
                mid = (left + right) // 2
                val = vec[mid]
                if val < num:
                    left = mid + 1
                else:
                    right = mid - 1
            vec[left] = num
            indices.append(left)
    max_len = len(vec) - 1
    print(max_len)
    last_idx = max_len
    longest_arr = []
    for i in range(N - 1, -1, -1):
        if indices[i] == last_idx:
            longest_arr.append(arr[i])
            last_idx -= 1
    print(*longest_arr[::-1])


if __name__ == '__main__':
    main()
