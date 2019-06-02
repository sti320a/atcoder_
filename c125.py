N = int(input())
As = list(map(int, input().split()))


def gcd(x, y):
    if x < y:
        x, y = y, x
    if y == 0:
        return x
    return gcd(x % y, y)


L = []
R = []

L.append(0)
R.append(0)

for i in range(N - 1):
    L.append(gcd(L[i], As[i]))
    R.append(gcd(R[i], As[N-i-1]))


ans = 0
for i in range(N):
    ans = max(ans, gcd(L[i], R[N-i-1]))

print(ans)
