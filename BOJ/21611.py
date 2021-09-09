# 1 10 27 52        왼
#  9  17 25
# 7+2,14+3,21+4

# 0, 7, 22, 45      위
#  7, 15,  23
#  7+0, 14+1, 21+2

# 0, 5, 18, 39      오
#  5, 13, 21
#  0+5, 7+6, 14+7,

# 0, 3, 14, 33      아
#   3, 11, 19
#  0+3, 7+4, 14+5

import sys
sys.stdin = open('../input.txt', 'r')

# 오른, 아래, 왼, 위
dx, dy = [0,1,0,-1], [1,0,-1,0]


def change_arr_to_list(arr):
    pos_x, pos_y = 0,0
    is_visited = [[False]*N for _ in range(N)]
    f_dir = 0
    ls_map = []
    for _ in range(N**2):
        ls_map.append(arr[pos_x][pos_y])
        is_visited[pos_x][pos_y] = True

        if f_dir == 0:
            if pos_y+1 == N or is_visited[pos_x][pos_y+1]:
                f_dir += 1
        elif f_dir == 1:
            if pos_x + 1 == N or is_visited[pos_x+1][pos_y]:
                f_dir += 1
        elif f_dir == 2:
            if pos_y - 1 == -1 or is_visited[pos_x][pos_y-1]:
                f_dir += 1
        elif f_dir == 3:
            if pos_x - 1 == -1 or is_visited[pos_x-1][pos_y]:
                f_dir = 0
        pos_x, pos_y = pos_x+dx[f_dir], pos_y+dy[f_dir]
    return list(reversed(ls_map))


def break_ball(ls_map, magic_dir, magic_dis):
    # print(ls_map, magic_dir, magic_dis)
    idx = 0
    cnt = 0     # 몇번째 수인지
    while idx < N**2 and cnt <= magic_dis:
        ls_map[idx] = 0
        if magic_dir == 1:      # 위
            # 0, 7, 22, 45, 76      위
            #  7, 15, 23, 31
            # 7+0,14+1,21+2,28+3
            idx += (7*(cnt+1)+cnt)
        elif magic_dir == 2:    # 아래
            # 0, 3, 14, 33      아
            #   3, 11, 19
            #  0+3, 7+4, 14+5
            idx += (7 * cnt + cnt+3)
        elif magic_dir == 3:    # 왼
            # 0 1 10 27 52        왼
            #  1 9  17 25
            # 0+1,7+2,14+3,21+4
            idx += (7 * cnt + cnt+1)
        elif magic_dir == 4:    # 오
            # 0, 5, 18, 39, 68      오
            #  5, 13, 21, 29
            #  0+5, 7+6, 14+7, 21 + 8
            idx += (7 * cnt + cnt+5)
        cnt += 1
    #print(magic_dis, cnt)

    return ls_map


def delete_zero(ls_map):
    # print(ls_map)
    new_ls = [0]*N**2
    idx_non_zero = 1
    for idx in range(1, N**2):
        if ls_map[idx] != 0:
            new_ls[idx_non_zero] = ls_map[idx]
            idx_non_zero += 1

    return new_ls


def delete_continuous_ball(ls_map):
    #print(ls_map)
    new_ls = [0]*N**2
    pos_prev = 1
    cnt = 1

    ball_cnt = 0

    for idx in range(2, N**2):
        if ls_map[idx] == ls_map[pos_prev]:
            cnt += 1
        else:
            if cnt >= 4:
                ball_cnt += ls_map[pos_prev]*cnt
                cnt = 1
                pos_prev = idx
            else:
                new_ls[pos_prev:pos_prev+cnt] = ls_map[pos_prev:pos_prev+cnt]
                cnt = 1
                pos_prev = idx


    #print(new_ls)
    return new_ls, ball_cnt


def change_to_group(ls_map):
    new_ls = [0]
    pos_prev = 1
    cnt = 1

    for idx in range(2, N ** 2):
        if ls_map[idx] == ls_map[pos_prev]:
            cnt += 1
        else:
            new_ls.append(cnt)
            new_ls.append(ls_map[pos_prev])
            cnt = 1
            pos_prev = idx
        if len(new_ls) > N ** 2:
            new_ls = new_ls[:N ** 2]
            break
    new_ls += [0]*(N**2-len(new_ls))
    # print(new_ls)
    return new_ls

N, M = map(int, input().split())
arr_map = [list(map(int,input().split())) for _ in range(N)]
# print(*arr_map, sep='\n')
arr_command = [list(map(int,input().split())) for _ in range(M)]
# print(*arr_command, sep='\n')

ls_map = change_arr_to_list(arr_map)
# print(ls_map)
ans = 0
#print(arr_command)

is_test = False

for i in range(M):
    ls_map = break_ball(ls_map, *arr_command[i])
    ls_map = delete_zero(ls_map)

    # ans_tmp = 0
    while True:
        ls_map, ans_tmp = delete_continuous_ball(ls_map)
        if not ans_tmp:
            break
        ans += ans_tmp
        ls_map = delete_zero(ls_map)

    ls_map = change_to_group(ls_map)

print(ans)
