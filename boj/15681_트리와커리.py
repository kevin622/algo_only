import sys

N, R, Q = map(int, input().split())
connections = {i: [] for i in range(1, N + 1)}
for _ in range(N - 1):
    U, V = map(int, input().split())
    connections[U].append(V)
    connections[V].append(U)

sizes = [1] * (N + 1)


def make_tree(current_node, parent):
    for node in connections[current_node]:
        if node != parent:
            make_tree(node, current_node)
            sizes[current_node] += sizes[node]


def main():
    sys.setrecursionlimit(N + 5)
    make_tree(R, -1)
    answer = []
    for _ in range(Q):
        u = int(input())
        answer.append(sizes[u])
    print('\n'.join(map(str, answer)))


if __name__ == '__main__':
    main()
