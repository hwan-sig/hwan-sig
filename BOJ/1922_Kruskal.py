import sys
sys.stdin = open('../input.txt', 'r')

N = int(input())
M = int(input())

ls_edge = [list(map(int,input().split())) for _ in range(M)]
ls_edge = sorted(ls_edge, key=lambda edge: edge[2])

# print(ls_edge)
check_parent = list(range(N+1))


def get_parent(node):
    if check_parent[node] != node:
        check_parent[node] = get_parent(check_parent[node])
    return check_parent[node]


def union_set(node_prev, node_next):
    parent_prev, parent_next = get_parent(node_prev), get_parent(node_next)
    if parent_prev < parent_next:
        check_parent[parent_next] = parent_prev
    else:
        check_parent[parent_prev] = parent_next
    pass


cost = 0

for edge in ls_edge:
    a,b,c = edge
    if a == b:
        continue
    if get_parent(a) != get_parent(b):
        union_set(a, b)
        cost += c
print(cost)
