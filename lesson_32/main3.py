n = int(input())
s = 0
for i in range(n):
    a = input()
    chislo1 = int(a[0])
    chislo2 = int(a[2])
    chislo3 = int(a[4])
    if chislo1 + chislo2 + chislo3 >= 2:
        s += 1
print(s)
