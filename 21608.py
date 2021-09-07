import sys
sys.stdin = open('input.txt', 'r')


dx = [0,0,-1,1]
dy = [1,-1,0,0]


def find_first(idx, num_like):
    near_idx, near_count = [0, 0], 0

    pos_near_like = []      # 인접한 학생 수를 가진 pos list
    num_near_count = 0      # 인접한 학생 수

    for i in range(N):
        for j in range(N):
            if arr_map[i][j] != -1:
                continue
            tmp_cnt = 0
            # arr이 -1중에 좋아하는 학생이 많은 칸을 선택.

            for f_dir in range(4):
                nx = i + dx[f_dir]
                ny = j + dy[f_dir]
                if nx<0 or nx>=N or ny<0 or ny>=N:
                    continue
                tmp_num = arr_map[nx][ny]
                if tmp_num == -1:
                    continue
                if tmp_num in num_like:
                    tmp_cnt += 1

            if num_near_count < tmp_cnt:
                pos_near_like = [[i, j]]
                num_near_count = tmp_cnt
            elif num_near_count == tmp_cnt:
                pos_near_like.append([i, j])

    return pos_near_like


def find_second(arr_idx):
    tmp_stu, empty_cnt = [0, 0], -1
    for idx in arr_idx:
        x, y = idx
        tmp_cnt = 0
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if arr_map[nx][ny] == -1:
                tmp_cnt += 1
        if empty_cnt < tmp_cnt:

            tmp_stu = idx
            empty_cnt = tmp_cnt

    return tmp_stu


N = int(input())
arr_map = [[-1]*N for _ in range(N)]

arr_stu = []
for _ in range(N**2):
    arr_stu.append(list(map(int, input().split())))

# print(arr_stu)
dict_stu = {}

for student in arr_stu:
    stu_idx = student[0]
    stu_like = student[1:]

    dict_stu[stu_idx] = stu_like

    idx = find_first(stu_idx, stu_like)
    if len(idx) > 1:
        idx = find_second(idx)
        arr_map[idx[0]][idx[1]] = stu_idx
    else:
        arr_map[idx[0][0]][idx[0][1]] = stu_idx


def calc_happy(dict_student):
    ans = 0
    points = [0,1,10,100,1000]
    for i in range(N):
        for j in range(N):
            cnt = 0
            for f_dir in range(4):
                nx, ny = i + dx[f_dir], j + dy[f_dir]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if arr_map[nx][ny] in dict_student[arr_map[i][j]]:
                    cnt += 1
            ans += points[cnt]
    return ans


print(calc_happy(dict_stu))