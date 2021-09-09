import heapq
from math import inf

V, E = map(int, input().split())
K = int(input())

dis_map = [[] for _ in range(1+V)]

for i in range(E):
    u, v, w = map(int, input().split())
    dis_map[u].append((v, w))

ans_dis = [inf]*(1+V)
ans_dis[K] = 0

heap = []
heapq.heappush(heap, (0, K))

while heap:
    cur_dis, cur_node = heapq.heappop(heap)
    if ans_dis[cur_node] < cur_dis:
        continue

    for next_node, next_w in dis_map[cur_node]:
        if cur_dis + next_w < ans_dis[next_node]:
            ans_dis[next_node] = cur_dis + next_w
            heapq.heappush(heap, (ans_dis[next_node], next_node))

ans = ''
for i in range(1, V+1):
    ans += 'INF\n' if ans_dis[i] == inf else f'{ans_dis[i]}\n'

print(ans)