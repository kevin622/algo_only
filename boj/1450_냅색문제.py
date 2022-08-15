import sys

input = sys.stdin.readline


# arr의 부분집합 구하는 함수
def subset(arr: list, max_sum: int):
    result = []
    for i in range(1 << len(arr)):
        sub_sum = 0
        is_over = False
        for j in range(len(arr)):
            if i & (1 << j):
                sub_sum += arr[j]
                if sub_sum > max_sum:
                    is_over = True
                    break
        if not is_over:
            result.append(sub_sum)
    result.sort()
    return result


def main():
    N, C = map(int, input().split())
    arr = list(map(int, input().split()))
    # 두 리스트로 나눠서 사용
    arr1, arr2 = arr[:N // 2], arr[N // 2:]
    subset1 = subset(arr1, C)
    subset2 = subset(arr2, C)
    # 각 리스트별로 다른 포인터 사용
    pointer1 = 0
    pointer2 = len(subset2) - 1
    answer = 0
    while pointer1 < len(subset1) and pointer2 >= 0:
        if subset1[pointer1] + subset2[pointer2] > C:
            pointer2 -= 1
        else:  # (subset1[pointer1] + subset2[pointer2]) <= C
            answer += pointer2 + 1
            pointer1 += 1
    print(answer)


if __name__ == '__main__':
    main()
