# 꼭 문제를 잘 읽자..
import sys
sys.stdin = open('../input.txt', 'r')
from collections import deque

N, M = map(int, input().split())
arr_map = [list(map(int, input().split())) for _ in range(N)]

# print(arr_map)
dx = [0,0,-1,1]
dy = [1,-1,0,0]


def find_block(arr_block):
    is_visited = [[False]*N for _ in range(N)]
    color_rep = [-1,-1,0,0]      # i, j, color_cnt, rainbow_cnt
    list_not_color = [-2, -1, 0]

    for i in range(N):
        for j in range(N):
            if arr_block[i][j] in list_not_color:
                continue
            if is_visited[i][j]:
                continue

            is_visited_rain = [[False]*N for _ in range(N)]
            color = arr_block[i][j]
            color_cnt = 1
            rainbow_cnt = 0

            Q = deque()
            Q.append([i, j])
            is_visited[i][j] = True

            while Q:
                x, y = Q.popleft()

                for f_dir in range(4):
                    nx, ny = x+dx[f_dir], y+dy[f_dir]
                    if not (0 <= nx < N and 0 <= ny < N):
                        continue

                    if arr_block[nx][ny] == color and not is_visited[nx][ny]:
                        Q.append([nx, ny])
                        color_cnt += 1
                        is_visited[nx][ny] = True
                    elif arr_block[nx][ny] == 0 and not is_visited_rain[nx][ny]:
                        Q.append([nx, ny])
                        color_cnt += 1
                        rainbow_cnt += 1
                        is_visited_rain[nx][ny] = True

            if color_cnt >= 2:
                if color_rep[2] < color_cnt:
                    color_rep = [i, j, color_cnt, rainbow_cnt]
                elif color_rep[2] == color_cnt:
                    if color_rep[3] < rainbow_cnt:
                        color_rep = [i, j, color_cnt, rainbow_cnt]
                    elif color_rep[3] == rainbow_cnt:
                        if color_rep[0] < i:
                            color_rep = [i, j, color_cnt, rainbow_cnt]
                        elif color_rep[0] == i:
                            if color_rep[1] < j:
                                color_rep = [i, j, color_cnt, rainbow_cnt]

    return color_rep


def delete_block(s_x,s_y,_1,_2):      # -2 는 deleted_value
    # print(x,y,num)
    Q = deque()
    Q.append([s_x,s_y])
    color = arr_map[s_x][s_y]
    arr_map[s_x][s_y] = -2

    while Q:
        x, y = Q.popleft()
        for f_dir in range(4):
            nx, ny = x + dx[f_dir], y + dy[f_dir]
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            if arr_map[nx][ny] in [0, color]:
                arr_map[nx][ny] = -2
                Q.append([nx, ny])

    return 0


def gravity(arr_map):
    """"
    가장 큰 row부터 col은 고정 2pos로 탐색
    위 값이 -1이면 down값은 pos_up -1의 위치로 옮긴다.
    위값이 비어있으면 -1반복
    위값이 있으면, down으로 이동.
    """
    for j in range(N):
        for pos_down in range(N-1, 0, -1):
            if arr_map[pos_down][j] != -2:
                continue

            for pos_up in range(pos_down-1, -1, -1):
                tmp_up = arr_map[pos_up][j]
                if tmp_up == -1:
                    break
                elif tmp_up == -2:
                    continue
                elif tmp_up >= 0:
                    arr_map[pos_down][j] = arr_map[pos_up][j]
                    arr_map[pos_up][j] = -2
                    break
    return 0


def rotation(arr_map):
    """
    격자 반시계 90도 회전

    :param arr_map:
    :return:    90도 회전한 새로운 N*N list
    """
    new_map = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_map[N-j-1][i] = arr_map[i][j]
    return new_map


def print_map(arr):
    for ls in arr:
        print(*ls, sep='\t')
    print()
    return 0


ans = 0
while True:
    represent_val = find_block(arr_map)  # 대표값 i,j, 개수
    if not represent_val[2]:
        break
    #print(represent_val)

    ans += represent_val[2]**2
    delete_block(*represent_val)
    #print_map(arr_map)

    gravity(arr_map)
    #print_map(arr_map)

    arr_map = rotation(arr_map)
    #print_map(arr_map)

    gravity(arr_map)
    #print_map(arr_map)

print(ans)