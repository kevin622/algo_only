import sys


def main():
    input = sys.stdin.readline
    V, E = map(int, input().split())
    # graph = {i: {} for i in range(1, V + 1)}
    connections = [list(map(int, input().split())) for _ in range(E)]
    connections.sort(key=lambda x: x[2])
    head = list(range(V + 1))

    def get_head(node: int):
        if head[node] != node:
            head[node] = get_head(head[node])
        return head[node]

    line_cnt = 0
    answer = 0
    idx = 0
    while line_cnt != V - 1:
        v1, v2, w = connections[idx]
        idx += 1
        v1_head = get_head(v1)
        v2_head = get_head(v2)
        if v1_head == v2_head:
            continue
        head[v2_head] = v1_head
        answer += w
        line_cnt += 1
    print(answer)


if __name__ == "__main__":
    main()
