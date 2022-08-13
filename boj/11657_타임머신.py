import sys

input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]

    # bellman-ford
    INF = 1e10
    distance = [INF] * (N + 1)
    # 시작점
    distance[1] = 0
    # 음수 순환이 존재하는지
    is_negative_circular = False
    # V번 반복, E개의 간선 모두 확인
    for j in range(N):
        for i in range(M):
            from_node, to_node, cost = edges[i]
            if distance[from_node] != INF:
                if (distance[from_node] + cost) < distance[to_node]:
                    distance[to_node] = distance[from_node] + cost
                    # 업데이트가 V번째 반복에서 발생했으면 음수 순환이 존재한다는 뜻
                    if j == (N - 1):
                        is_negative_circular = True

    if is_negative_circular:
        print(-1)
    else:
        for i in range(2, N + 1):
            if distance[i] == INF:
                print(-1)
            else:
                print(distance[i])


if __name__ == '__main__':
    main()
