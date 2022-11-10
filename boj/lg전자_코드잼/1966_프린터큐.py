import sys
from collections import deque


def main():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        importances = deque([(i, importance) for i, importance in enumerate(map(int, input().split()))])
        importance_cnt = {i: 0 for i in range(1, 10)}
        order = 1
        max_importance = 0
        for i in range(N):
            importance = importances[i][1]
            importance_cnt[importance] += 1
            max_importance = max(max_importance, importance)

        while importances:
            idx, importance = importances.popleft()
            if importance < max_importance:
                importances.append((idx, importance))
            else:
                if idx == M:
                    break
                else:
                    importance_cnt[max_importance] -= 1
                    order += 1
                    while importance_cnt[max_importance] == 0:
                        max_importance -= 1
        print(order)


if __name__ == '__main__':
    main()
