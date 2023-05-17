s  = input().split(' ')
s, steps = int(s[0]), int(s[1])

for i in range(steps):
    if s % 10 !=0:
        s-=1
    else:
        s//=10
print(s)

