def solution(queue1, queue2):
    summed = sum(queue1) + sum(queue2)
    if summed % 2 == 1:
        return -1
    half = summed // 2
    if max(queue1) > half or max(queue2) > half:
        return -1

    queue = [0] + queue1 + queue2
    for i in range(2, len(queue)):
        queue[i] += queue[i - 1]
    l = 0
    r = 1
    min_cnt = 1e9
    while r < len(queue):
        val = queue[r] - queue[l]
        if val < half:
            r += 1
        elif val > half:
            l += 1
        else:
            if l <= len(queue1):
                if r < len(queue1):
                    cnt = r + len(queue2) + l
                elif r == len(queue1):  # 빼먹은 조건...ㅠㅠ
                    cnt = l
                else:
                    cnt = l + r - len(queue1)
            else:
                cnt = r + l - len(queue1)
            min_cnt = min(cnt, min_cnt)
            l += 1
            r += 1

    answer = min_cnt if min_cnt != 1e9 else -1
    return answer


if __name__ == '__main__':
    print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
