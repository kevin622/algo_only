import sys
import heapq

INF = float("inf")


def main():
    input = sys.stdin.readline
    V, E = map(int, input().split())
    K = int(input().strip())
    graph = {i: {} for i in range(1, V + 1)}
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u][v] = min(graph[u].get(v, 100), w)

    # dijkstra
    distances = [INF] * V
    heap = [(0, K)]
    while heap:
        distance, node = heapq.heappop(heap)
        if distance < distances[node - 1]:
            distances[node - 1] = distance
            for n_node in graph[node]:
                if graph[node][n_node] + distance < distances[n_node-1]:
                    heapq.heappush(heap, (graph[node][n_node] + distance, n_node))
    print('\n'.join(map(lambda x: str(x).upper(), distances)))


if __name__ == "__main__":
    main()
