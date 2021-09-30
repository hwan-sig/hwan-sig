import sys
#sys.stdin = open('../input.txt', 'r')
from collections import deque

'''
-- 
1-,-1,--

1-,
-1, --

-1,
1-, --

1,1,1,
*3,*2,*2


'''
N = int(input()) - 1
ans = [[1]*2 for _ in range(3)]
for j in range(N):
    col = j % 2
    ans[0][col] = ans[0][col - 1] + ans[1][col - 1] + ans[2][col - 1]
    ans[1][col] = ans[0][col - 1] + ans[2][col - 1]
    ans[2][col] = ans[0][col - 1] + ans[1][col - 1]
col = (N+1) % 2
res = ans[0][col] + ans[1][col] + ans[2][col]
print(res%9901)