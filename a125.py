A, B, T = map(int, input().split())

sum = 0
for s in range(1, T+1):
    if s % A == 0:
        sum += B

print(sum)
