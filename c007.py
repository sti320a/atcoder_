from collections import deque

# r: 行数 c: 列数
r, c = map(int, input().split())

# スタート地点の座標
sy, sx = map(int, input().split())

# ゴール地点の座標
gy, gx = map(int, input().split())

# 迷路自体（行数だけinputする）
maze = [input() for _ in range(r)]

# 移動を表現
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


# dequeはキューを生成する [スタートy, スタートx, 距離=0]
q = deque([(sy-1, sx-1, 0)])

# メモ用の配列を生成
memo = [[0 for _ in range(c)] for __ in range(r)]

while q:
    # popleft() 先頭要素の取り出し, dist: 距離
    y, x, dist = q.popleft()

    # dx, dy で移動を表現する
    for x_, y_ in zip(dx, dy):
        # 移動した先が . (=進めるところ)で、かつ、メモになかったら
        if maze[y + y_][x + x_] == '.' and memo[y + y_][x + x_] == 0:
            # メモに距離を記録
            memo[y + y_][x + x_] = dist + 1
            # キューに移動後の座標とそこまでの距離を記録
            q.append((y + y_, x + x_, dist + 1))


print(memo[gy-1][gx-1])
