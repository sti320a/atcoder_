s = input()
s = list(s)


if len(s) < 15:
    for _ in range(15-len(s)):
        s.append('o')

cnt = 0
for r in s:
    if r == 'o':
        cnt += 1

if cnt >= 8:
    print('YES')
else:
    print('NO')
