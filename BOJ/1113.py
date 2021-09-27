# 핵심 idea, 물이 담기는 곳은 4면이 막혀져 있는 곳이다.

import sys
sys.stdin = open('../input.txt', 'r')
from collections import deque


N, M = map(int, input().split())
arr_map = [list(map(int,input())) for _ in range(N)]
dx, dy = [0,0,-1,1], [1,-1,0,0]


def make_floor(floor: int):
    water_arr = [[True] * (M+2) for _ in range(N+2)]
    block_count = 0
    for i in range(N):
        for j in range(M):
            if arr_map[i][j] >= floor:
                water_arr[i+1][j+1] = False
                block_count += 1
    return water_arr, block_count


def is_inside(x, y):
    return 0<=x<N+2 and 0<=y<M+2


def count_side_water(water_map):
    is_visited = [[False] * (M+2) for _ in range(N+2)]
    Q = deque([[0,0]])
    is_visited[0][0] = True
    water_count = 1

    while Q:
        x, y = Q.popleft()
        for f_dir in range(4):
            nx, ny = x+dx[f_dir], y+dy[f_dir]
            if not is_inside(nx, ny):
                continue
            if not is_visited[nx][ny] and water_map[nx][ny]:
                Q.append([nx, ny])
                is_visited[nx][ny] = True
                water_count += 1
    return water_count

res = 0
for floor in range(2, 10):
    water_map, block_count = make_floor(floor)

    if block_count == 0:
        break
    #print(floor,*water_map, sep='\n')
    # print()
    water_count = count_side_water(water_map)
    res += (M+2)*(N+2) - water_count - block_count
print(res)