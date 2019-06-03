N, A, B, C, D = map(int, input().split())
S = input()

"""
7 1 3 7 6
.#..#..
A#B.#CD
"""

if C < D:
    cnt = 0
    for i in range(len(S)):
        if i >= len(S) - 1:
            break
        if S[i] == "#" and S[i+1] == "#":
            cnt += 1
    if cnt >= 1:
        print('No')
    else:
        print('Yes')

if C > D:
    cnt = 0
    for i in range(B, D):
        if S[i-1] == '.' and S[i] == '.' and S[i+1] == '.':
            cnt += 1
    if cnt >= 1:
        print('Yes')
    else:
        print('No')
