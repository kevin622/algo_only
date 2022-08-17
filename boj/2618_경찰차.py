# 참고: https://yabmoons.tistory.com/644
import sys

input = sys.stdin.readline
sys.setrecursionlimit(1005)
N = int(input())
W = int(input())
coors = [list(map(int, input().split())) for _ in range(W)]
# dp[i][j] = k 의 의미: 1번 차가 i번 사건을 해결하고 2번 차가 j번 사건을 해결했을 때,
# 두 차가 남은 사건을 모두 해결하는 최소의 거리합이 k라는 뜻
dp = [[-1] * (W + 1) for _ in range(W + 1)]


def get_distance(r1: int, c1: int, r2: int, c2: int) -> int:
    return abs(r1 - r2) + abs(c1 - c2)


def get_total_distance(car1: int, car2: int) -> int:
    # car1, car2는 각각 1번차, 2번차가 마지막으로 해결한 사건 번호
    if car1 == W or car2 == W:
        dp[car1][car2] = 0
        return 0
    if dp[car1][car2] != -1:
        return dp[car1][car2]

    # 다음 사건 번호
    next_case_idx = max(car1, car2) + 1
    r, c = coors[next_case_idx - 1]

    # 다음 사건 위치까지 1번차와 2번차의 거리
    dist1 = get_distance(r, c, 1, 1) if car1 == 0 else get_distance(r, c, *coors[car1 - 1])
    dist2 = get_distance(r, c, N, N) if car2 == 0 else get_distance(r, c, *coors[car2 - 1])

    result1 = dist1 + get_total_distance(next_case_idx, car2)
    result2 = dist2 + get_total_distance(car1, next_case_idx)
    dp[car1][car2] = min(result1, result2)

    return dp[car1][car2]


def print_route(car1: int, car2: int):
    if car1 == W or car2 == W:
        return

    # 다음 사건 번호
    next_case_idx = max(car1, car2) + 1
    r, c = coors[next_case_idx - 1]

    # 다음 사건 위치까지 1번차와 2번차의 거리
    dist1 = get_distance(r, c, 1, 1) if car1 == 0 else get_distance(r, c, *coors[car1 - 1])
    dist2 = get_distance(r, c, N, N) if car2 == 0 else get_distance(r, c, *coors[car2 - 1])

    if (dp[next_case_idx][car2] + dist1) < (dp[car1][next_case_idx] + dist2):
        print(1)
        print_route(next_case_idx, car2)
    else:
        print(2)
        print_route(car1, next_case_idx)


def main():
    get_total_distance(0, 0)
    print(dp[0][0])
    print_route(0, 0)


if __name__ == '__main__':
    main()
