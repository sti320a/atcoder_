a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

k = int(input())

ls = [a, b, c, d, e]

ans = 'Yay!'
for l in ls:
    for n in ls:
        if l - n > k:
            ans = ':('

print(ans)
