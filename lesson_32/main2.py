n = int(input())
for i in range(n):
    b = input()
    if len(b) > 10:
        p1 = b[0]
        p2 = len(b) - 2
        p3 = b[-1]
        result = f'{p1}{p2}{p3}'
        print(result)
    else:
        result = b
        print(result)