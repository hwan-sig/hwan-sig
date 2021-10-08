import sys
sys.stdin = open('../input.txt', 'r')
from queue import PriorityQueue

N = int(input())
# arr_map = [list(map(int, input().split())) for _ in range(N)]
arr_map = [[1,2,3] for _ in range(N)]

max_val = arr_map[0].copy()
min_val = arr_map[0].copy()

for i in range(1, N):
    a,b,c = max_val
    max_val[0] = max(a,b) + arr_map[i][0] # arr_map[i-1][0], arr_map[i-1][1], max_val[0])
    max_val[1] = max(a,b,c) + arr_map[i][1]
    max_val[2] = max(b,c) + arr_map[i][2]
    # print(max_val, max(max_val))

    a,b,c = min_val
    min_val[0] = min(a, b) + arr_map[i][0]
    min_val[1] = min(a, b, c) + arr_map[i][1]
    min_val[2] = min(b, c) + arr_map[i][2]
    # print(min_val, min(min_val))

print(max(max_val), min(min_val))