import sys
sys.stdin = open('../input.txt', 'r')
from collections import deque

# pos(x,y,z)저장, 방향.

class Pos:
    def __init__(self, line: str, arr: deque, num: int, arr_map: list):
        x, y, f_dir = map(int, line.split())
        self.x = x-1
        self.y = y-1
        # self.z = 0          # 딱히 쓸모없어 보임
        # self.color = arr_map[x-1][y-1]      # 흰, 빨, 파 => 0, 1, 2
        self.f_dir = f_dir-1

        arr[x-1][y-1].append(num)

    def qprint(self):
        print('x:', self.x, ' y:', self.y, ' fdir:', self.f_dir,)# ' color:', self.color)

    def getitem(self):
        return self.x, self.y, self.f_dir

dx, dy = [0,0,-1,1], [1,-1,0,0]

N, M = map(int,input().split())
arr_map = [list(map(int,input().split())) for _ in range(N)]
arr_que = [[deque() for _ in range(N)] for _ in range(N)]    # 체스말의 쌓여있는 말을 저장
arr_pos = [Pos(input(), arr_que, _, arr_map) for _ in range(M)]      # Pos Class를 저장, [x,y,z,f_dir]


#arr_pos[0].qprint()
#print(*arr_que, sep='\n')


def move_white(x,y,nx,ny,idx):
    tmp_stack = []
    while arr_que[x][y][-1] != idx:
        new_idx = arr_que[x][y].pop()
        #print('white', new_idx)
        arr_pos[new_idx].x = nx
        arr_pos[new_idx].y = ny

        tmp_stack.append(new_idx)
    new_idx = arr_que[x][y].pop()
    #print('white', new_idx)
    arr_pos[new_idx].x = nx
    arr_pos[new_idx].y = ny

    tmp_stack.append(new_idx)

    # print(tmp_stack)

    while tmp_stack:
        arr_que[nx][ny].append(tmp_stack.pop(-1))

    if len(arr_que[nx][ny]) >= 4:
        global break_flag
        break_flag = True

    #print(*arr_que, sep='\n')


def move_red(x,y,nx,ny,idx):
    tmp_top_idx = arr_que[x][y][-1]
    while arr_que[x][y][-1] != idx:
        new_idx = arr_que[x][y].pop()
        #print('white', new_idx)
        arr_pos[new_idx].x = nx
        arr_pos[new_idx].y = ny

        arr_que[nx][ny].append(new_idx)
    new_idx = arr_que[x][y].pop()
    #print('white', new_idx)
    arr_pos[new_idx].x = nx
    arr_pos[new_idx].y = ny

    arr_que[nx][ny].append(new_idx)

    if len(arr_que[nx][ny]) >= 4:
        global break_flag
        break_flag = True

    #(*arr_que, sep='\n')


def move_blue(x,y,f_dir,idx):
    new_fdir = change_dir(f_dir)
    nx,ny = x+dx[new_fdir], y+dy[new_fdir]

    arr_pos[idx].f_dir  = new_fdir

    next_color = get_color(nx, ny)  # arr_map[nx][ny]
    if next_color == 0:
        move_white(x, y, nx, ny, idx)
    elif next_color == 1:
        move_red(x, y, nx, ny, idx)


def get_color(x, y):
    return arr_map[x][y] if 0<=x<N and 0<=y<N else 3


def change_dir(f_dir):
    if f_dir == 0:
        res = 1
    elif f_dir == 1:
        res = 0
    elif f_dir == 2:
        res = 3
    elif f_dir == 3:
        res = 2
    return res


def start():

    global break_flag
    break_flag = False

    # print(*arr_que, sep='\n')

    for cnt in range(1000):
        for idx, pos in enumerate(arr_pos):
            x,y,f_dir = pos.getitem()
            #print(x,y,f_dir)
            nx, ny = x+dx[f_dir], y+dy[f_dir]
            #print('nx,ny:',nx,ny)
            next_color = get_color(nx,ny) # arr_map[nx][ny]
            if next_color == 0:
                move_white(x,y,nx,ny,idx)
            elif next_color == 1:
                move_red(x,y,nx,ny,idx)
            elif next_color >= 2:
                move_blue(x, y, f_dir, idx)
                #print(f_dir)
        if break_flag:
            print(cnt+1)
            break
    else:
        print(-1)


break_flag = False
start()