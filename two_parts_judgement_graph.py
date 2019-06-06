from collections import defaultdict

N, M = map(int, input().split())
dict = defaultdict(set)

for i in range(M):
    a, b = list(map(int, input().split()))
    dict[a].add(b)
    dict[b].add(a)

color = [0 for i in range(N+1)]
res = 'Yes'


def dfs(v, c, queue=[]):
    global color
    global res
    queue.append(v)

    for i in list(dict[v]):
        if color[i] == c:
            res = 'No'
        elif i not in queue:
            color[i] = c*-1
            dfs(i, -c, queue)


color[1] = 1
(dfs(1, 1))
print(res)
