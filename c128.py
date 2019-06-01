N, M = map(int, input().split())
ks = [list(map(int, input().split())) for _ in range(M)]

ps = list(map(int, input().split()))

ans = 0

"""
s0, s1, s2, ... , sn
d0, d1, d2, ... , dm
"""

for i in range(2**N):
    light = 0
    for j in range(M):
        cnt = 0
        for k in range(1, ks[j][0]+1):
            if i & 2**(ks[j][k]-1) == 2**(ks[j][k]-1):
                cnt += 1
        if cnt % 2 == ps[j]:
            light += 1

    if light == M:
        ans += 1

print(ans)
