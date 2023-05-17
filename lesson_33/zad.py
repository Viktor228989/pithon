counter = 0
a = int(input())
for i in range(5, 0, -1):
    while a >= i:
        a -= i
        counter += 1
print(counter)