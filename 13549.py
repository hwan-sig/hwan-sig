import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

N, K = map(int, input().split())

que = deque()
next_q = deque()

que.append(N)  # time, pos

arr_time = [-1]*(1+100000)
arr_time[N] = 0

while que:
    cur_pos = que.popleft()
    cur_time = arr_time[cur_pos]
    next_pos = cur_pos * 2

    while next_pos <= 100000 and arr_time[next_pos] == -1:
        que.append(next_pos)
        arr_time[next_pos] = cur_time
        next_pos *= 2

    if cur_pos-1 >= 0 and arr_time[cur_pos-1] == -1:
        next_q.append(cur_pos-1)
        arr_time[cur_pos-1] = cur_time+1
    if cur_pos+1 <= 100000 and arr_time[cur_pos+1] == -1:
        next_q.append(cur_pos+1)
        arr_time[cur_pos+1] = cur_time+1
    if arr_time[K] != -1:
        print(arr_time[K])
        break
