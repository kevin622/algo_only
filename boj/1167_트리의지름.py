import sys


def main():
    input = sys.stdin.readline
    V = int(input())
    connections = {i: {} for i in range(1, V + 1)}
    for _ in range(V):
        arr = list(map(int, input().split()))
        vertex = arr[0]
        for i in range(1, len(arr), 2):
            if arr[i] == -1:
                break
            connections[vertex][arr[i]] = arr[i + 1]

    visited = [0] * (V + 1)
    stack = [(1, 1)]
    farthest_vertex = -1
    farthest_distance = -1
    while stack:
        v, distance = stack.pop()
        if distance > farthest_distance:
            farthest_distance = distance
            farthest_vertex = v
        if not visited[v]:
            visited[v] = 1
            for next_v in connections[v]:
                if not visited[next_v]:
                    stack.append((next_v, distance + connections[v][next_v]))

    visited = [0] * (V + 1)
    stack = [(farthest_vertex, 1)]
    farthest_distance = -1
    while stack:
        v, distance = stack.pop()
        if distance > farthest_distance:
            farthest_distance = distance
        if not visited[v]:
            visited[v] = 1
            for next_v in connections[v]:
                if not visited[next_v]:
                    stack.append((next_v, distance + connections[v][next_v]))
    print(farthest_distance - 1)


if __name__ == '__main__':
    main()
