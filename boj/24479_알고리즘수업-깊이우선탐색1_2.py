'''
dfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
    visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
    for each x ∈ E(R)  # E(R) : 정점 R의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
        if (visited[x] = NO) then dfs(V, E, x);
}
'''

import sys


def main():
    input = sys.stdin.readline
    N, M, R = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    for i in range(1, N + 1):
        graph[i].sort(reverse=True)
    visited = [0] * (N + 1)

    # dfs
    stack = [R]
    cnt = 1
    while stack:
        r = stack.pop()
        if not visited[r]:
            visited[r] = cnt
            cnt += 1
            for n_r in graph[r]:
                if not visited[n_r]:
                    stack.append(n_r)
    for i in range(1, N + 1):
        print(visited[i])


if __name__ == "__main__":
    main()
