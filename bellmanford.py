def BellmanFord(num_vertex, edges, source):
    inf = float('inf')

    # ある頂点までの距離（コスト）を記録するリスト
    costs = [inf for i in range(num_vertex)]
    costs[source-1] = 0

    for i in range(num_vertex):
        for edge in edges:

            # その辺の始点の頂点
            start = costs[edge[0]-1]
            # その辺の終点の頂点
            goal = costs[edge[1]-1]
            # コスト、距離、重み
            cost = edge[2]

            # 辺の緩和（よりコストの小さい経路を見つけたらリストを更新する）
            if edge[0] != inf and start + cost < goal:
                costs[edge[1]-1] = start + cost

                # 負閉路の検出
                if i == num_vertex-1:
                    return -1

    return costs
