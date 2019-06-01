N, K = map(int, input().split())

ans = 0
for i in range(1, N+1):
    tmp = 1
    while i * tmp < K:
        tmp *= 2
    ans += 1 / tmp

print(ans / N)
