# N: 宝石の数　K: 操作できる回数
N, K = map(int, input().split())
# 宝石たちの価値
V = list(map(int, input().split()))


# 解：宝石の価値の合計
ans = 0

# 宝石の数と操作できる数で小さい方を選び、その数だけ繰り返し
for n in range(1, min(K, N)+1):
    # (操作できる回数 - 操作回数), 操作回数 で小さい方を記録
    m = min(K-n, n)
    for l in range(n+1):
        # 操作回数
        r = n-l
        # 左からl番目までの宝石と右から r番目までの宝石を格納
        S = V[:l] + (V[-r:] if r != 0 else [])
        # ソートする
        S.sort()

        an = 0
        for i, a in enumerate(S):
            if i < m and a < 0:
                continue
            else:
                an += a
        ans = max(ans, an)

print(ans)
