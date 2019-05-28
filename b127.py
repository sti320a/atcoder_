r, D, x2 = map(int, input().split())

for _ in range(0, 10):
    nx = r * x2 - D
    print(nx)
    x2 = nx
