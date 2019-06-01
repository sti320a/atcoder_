N, M = map(int, input().split())

L, R = 1, N

for _ in range(M):
    a, b = list(map(int, input().split()))
    L = max(a, L)
    R = min(b, R)

print(max(0, R-L+1))
