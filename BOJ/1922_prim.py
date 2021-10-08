import sys
sys.stdin = open('../input.txt')
import heapq
from collections import deque


# input = sys.stdin.readline

N = int(input())
M = int(input())

weights = [float('INF')]*(N+1)
# print(weights)

ls_nodes = [deque() for _ in range(N+1)]
is_visited = [False]*(N+1)

for _ in range(M):
    a,b,c = map(int, input().split())
    if a == b:
        continue
    ls_nodes[a].append([b, c])
    ls_nodes[b].append([a, c])

# ls_edge = [list(map(int,input().split())) for _ in range(M)]

weights[1] = 0
heap = []
heapq.heappush(heap, [0, 1])    # weight, node,

while heap:
    weight, node = heapq.heappop(heap)
    if is_visited[node]:
        continue

    is_visited[node] = True

    for que in ls_nodes[node]:
        next_node, next_weight = que

        if weights[next_node] > next_weight and not is_visited[next_node]:

            weights[next_node] = next_weight
            heapq.heappush(heap, [next_weight, next_node])  # node, weight

print(sum(weights[1:]))
