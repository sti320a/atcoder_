A, B = map(int, input().split())

num = max(A, B)

if A == B:
    print(num + num)
else:
    print(num + num - 1)
