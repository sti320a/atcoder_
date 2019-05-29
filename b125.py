N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))

sum = 0

for i in range(N):
    if V[i] - C[i] > 0:
        sum += V[i] - C[i]

print(sum)
