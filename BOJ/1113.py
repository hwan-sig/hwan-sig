# 핵심 idea, 물이 담기는 곳은 4면이 막혀져 있는 곳이다.

import sys
sys.stdin = open('../input.txt', 'r')
from collections import deque


N, M = map(int, input().split())
arr_map = [list(map(int,input())) for _ in range(N)]
is_no_water = [[False]*M for _ in range(N)]

is_visited = [[False] * M for _ in range(N)]

dx, dy = [0,0,-1,1], [1,-1,0,0]


def is_inside(x, y):
    return 0<=x<N-1 and 0<=y<M-1


def check_no_water():
    p = []
    for i in range(N):
        for j in range(M):
            if is_no_water[i][j]:
                continue
            if 0 == i or N-1 == i or 0 == j or M-1 == j:
                is_no_water[i][j] = True
                Q = deque([[i, j]])
                while Q:
                    x, y = Q.popleft()
                    for f_dir in range(4):
                        nx, ny = x+dx[f_dir], y+dy[f_dir]
                        if not is_inside(nx, ny) or is_no_water[nx][ny]:
                            continue
                        if arr_map[nx][ny] >= arr_map[x][y]:
                            is_no_water[nx][ny] = True
                            Q.append([nx, ny])
                        elif not is_visited[nx][ny]:
                            is_visited[nx][ny] = True
                            p.append([nx,ny])
    print('p:',p)


def find_water_pos():
    pos = []
    for i in range(N):
        for j in range(M):
            if not is_no_water[i][j]:
                pos.append([i,j])
    return pos


check_no_water()
print(*is_no_water, sep='\n')
pos_water = find_water_pos()
print(pos_water)

Q = deque(pos_water)
print(Q)

"""
bfs로 채우면서 가장 높이가 낮은 is_no_water을 찾는다.
각 bfs의 영역의 높이는 (no_water의 높이 - 현재 높이) * 영역 로 찾는다.
"""


def cal_height(pos_water: deque):
    sum_height = 0

    while pos_water:
        _x, _y = pos_water.popleft()
        if is_visited[_x][_y]:
            continue

        is_visited[_x][_y] = True
        que_water_area = deque([[_x, _y]])
        ls_water_height = [arr_map[_x][_y]]
        min_height = 9
        while que_water_area:
            x, y = que_water_area.popleft()
            for f_dir in range(4):
                nx, ny = x + dx[f_dir], y + dy[f_dir]
                if is_no_water[nx][ny]:
                    min_height = min(min_height, arr_map[nx][ny])
                else:
                    if not is_visited[nx][ny]:
                        que_water_area.append([nx,ny])
                        is_visited[nx][ny] = True
                        ls_water_height.append(arr_map[nx][ny])
        print(ls_water_height)
        sum_height += min_height*len(ls_water_height) - sum(ls_water_height)
    print(*is_visited, sep='\n')
    return sum_height


print(cal_height(Q))