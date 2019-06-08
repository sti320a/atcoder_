INF = float('inf')


def Bellmanford(node, edges, source):
    d = [INF] * node  # ある頂点までのコストを保存するリスト
    d[source] = 0

    for i in range(node):
        for start, goal, cost in edges:
            # 辺の始まりの頂点までのコストが INF でなく
            # 辺の向かう先の頂点のコストが、より軽くなる場合に、
            # リストを更新する
            if d[start] != INF and d[start] + cost < d[goal]:
                d[goal] = d[start] + cost
                # 閉路を検出したらinfを返す
                if i == node-1 and goal == node-1:
                    return 'inf'
    return -d[node-1]


N, M = map(int, input().split())
abc = [map(int, input().split()) for _ in range(M)]
Edges = [None] * M

for i in range(M):
    ai, bi, ci = abc[i]
    Edges[i] = (ai-1, bi-1, -ci)


ans = Bellmanford(N, Edges, 0)
print(ans)
