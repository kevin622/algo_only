import sys

input = sys.stdin.readline


def main():
    V, E = map(int, input().split())
    connections = [tuple(map(int, input().split())) for _ in range(E)]

    # MST
    connections.sort(key=lambda x: x[2])
    set_roots = list(range(V + 1))

    def get_set(v):
        if set_roots[v] != v:
            set_roots[v] = get_set(set_roots[v])
        return set_roots[v]

    edge_cnt = 0
    cost_sum = 0
    for v1, v2, cost in connections:
        v1_set = get_set(v1)
        v2_set = get_set(v2)
        if v1_set != v2_set:
            set_roots[v2_set] = v1_set
            edge_cnt += 1
            cost_sum += cost
            if edge_cnt == (V - 1):
                sys.stdout.write(cost_sum)
                break


if __name__ == '__main__':
    main()
