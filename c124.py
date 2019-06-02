def solve(init, s):
    ideal = init  # 初期値 黒 or 白
    result = 0  # 塗り替える数
    for color in s:
        if color != ideal:
            result += 1
        ideal ^= 1  # 排他的論理和, 白黒逆になる
    return result


s = input()
s = list(map(int, s))
print(min(solve(0, s), solve(1, s)))
