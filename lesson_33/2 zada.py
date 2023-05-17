n = int(input())
s = input()
s = list(s)
i = 0
count = 0
while i != (len(s)-1):
    if s[i] == s[i+1]:
        s.pop(i)
        count +=1
    else:
        i +=1
print(count)
