import sys

input = sys.stdin.readline
sys.setrecursionlimit(int(500000))

K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    connections = {i: [] for i in range(1, V + 1)}
    for _ in range(E):
        v1, v2 = map(int, input().split())
        connections[v1].append(v2)
        connections[v2].append(v1)
    visited = [0] * (V + 1)
    answer = 'YES'


    def dfs(v, color):
        global answer
        if answer == 'NO':
            return
        if not visited[v]:
            visited[v] = color
            next_color = 1 if color == 2 else 2
            for next_v in connections[v]:
                if visited[next_v] == color:
                    answer = 'NO'
                    return
                elif not visited[next_v]:
                    dfs(next_v, next_color)


    for i in range(1, V + 1):
        if answer == 'NO':
            break
        elif not visited[i]:
            dfs(i, 1)
    print(answer)
