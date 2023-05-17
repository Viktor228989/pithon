a = input().split(" ")
nach = int(a[0])
den = int(a[1])
kolvo = int(a[2])
counter = 0
for i in range(1, kolvo + 1):
    counter += nach * i
if counter > den:
    counter -= den
    print(counter)
else:
    print(0)