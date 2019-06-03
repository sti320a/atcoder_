import re

s = input()
s = re.sub('BC', 'D', s)

ans = 0
cnt = 0
for c in s:
    if c == 'A':
        cnt += 1
    elif c == 'D':
        ans += cnt
    else:
        cnt = 0

print(ans)
