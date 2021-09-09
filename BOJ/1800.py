import sys
sys.stdin = open('../input.txt', 'r')
from queue import PriorityQueue

"""
다익스트라 + 이진탐색

다익스트라를 통해 P개보다 작은 개수의 선을 연결한다.

다익스트라를 통해 최소 가중치를 찾았더라도, 최대가중치를 K를 통해 지울 수 있다..
이것을 어떻게 해결할거임?

P개보다 작은 수의 케이블개수를 이진탐색 후, 해당 개수보다 작은 개수로 탐색할 수 있늕지 확인
P/2로 탐색 후 안되면 LOW를 올리고, 되면 

가격을 기준으로 이진탐색,
가격 => 주인이 내는 최소금액.
이 금액보다 같거나 작아야 함.
COST를 0으로 변경, 크면 1로 변경, 1의 합이 K보다 작아야 함.
작으면 COST를 줄인다. 
합이 크면, COST를 늘린다..

다익스트라를 통해 해당 COST에서 N에 도달가능한지 확인
"""

N, P, K = map(int, input().split())
# arr_map = [list(map(int, input().split())) for i in range(P)]
arr_map = [[] for _ in range(N+1)]

for i in range(P):
    a,b,c = map(int, input().split())
    arr_map[a].append([b, c])
    arr_map[b].append([a, c])


def Dijkstra(arr_cost, mid_cost):
    dis_visit = [float('inf')] * (N+1)
    que = PriorityQueue()
    tmp_cost = 0        # cost가 mid_cost보다 큰지 작은지. 0 or 1
    que.put([0, 1])     # distance, node
    dis_visit[0] = 0
    while not que.empty():
        cur_dis, cur_n = que.get()

        for next_n, next_w in arr_cost[cur_n]:
            if next_w <= mid_cost:
                tmp_cost = 0
            else:
                tmp_cost = 1

            if dis_visit[next_n] > cur_dis + tmp_cost:
                dis_visit[next_n] = cur_dis + tmp_cost
                que.put([dis_visit[next_n], next_n])

    return dis_visit[N] <= K

ans = -1
low, high = 0, 1000000
while low <= high:
    mid = (low + high) // 2
    is_possible = Dijkstra(arr_map, mid)
    if is_possible:
        ans = mid
        high = mid-1
    else:
        low = mid+1

print(ans if ans > -1 else -1)