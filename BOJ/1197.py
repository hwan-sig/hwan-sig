import sys
sys.stdin = open('../input.txt', 'r')


def get_parent(node):
    if parent_node[node] != node:
        parent_node[node] = get_parent(parent_node[node])
    return parent_node[node]

def set_parent(node, par):
    if parent_node[node] != node:
        parent_node[node] = par
        set_parent(parent_node[node], par)

V, E = map(int, input().split())
arr_map = []

for i in range(E):
    a, b, c = map(int, input().split())
    arr_map.append([c,a,b])

arr_map = sorted(arr_map, key=lambda t: t[0])
# print(arr_map)

parent_node = list(range(V+1))
res = 0
edge_cnt = 0
for edge in arr_map:
    cost, a, b = edge
    if get_parent(a) != get_parent(b):
        if parent_node[a] < parent_node[b]:
            parent_node[get_parent(b)] = parent_node[a]
        else:
            parent_node[get_parent(a)] = parent_node[b]

        res += cost
        edge_cnt += 1
        if edge_cnt == V-1:
            break
#print(parent_node)
print(res)