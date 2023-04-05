# Задача 2
#
# a = input("Начало первого урока (чч:мм) :")
# b = int(input("Длительность урока (мин) :"))
# c = int(input("Длительность перемен (мин) :"))
# d = int(input("На сколько уроков нужно расписание :"))
# e = int (a[:2])
# f = int(a[3:])
# time = e*60 + f
# for i in range(d):
#     e = time//60
#     f = time % 60
#     print(f"{i+1} урок: {str(e).rjust(2,'0')}:{str(f).rjust(2, '0')} - ", end='')
#     time+=b
#     print(f"{str(e).rjust(2, '0')}:{str(f).rjust(2, '0')}")
#     time +=c

#
# a = int(input("Сколько зомби было к началу расчёта:"))
# b = int(input("Сколько каждый может заразить:"))
# c = int(input("На который день делаем расчёт:"))
# #print(a*b)
# for i in range(c):
#     print(a)
#     a = a + a * b

a = input().split(' ')
a = list(map(int, a))
print(a)
def boba(a):
    lt = []
    for ind, elem in enumerate (a):
        if ind == 0: # первый элемент
            sssr = a[len(a)-1] + a[ind+1]
        elif ind == len(a)-1:# послдений элемент
            sssr = a[ind-1] + a[0]
        else:
            sssr = a[ind-1]+a[ind+1]
        lt.append(sssr)
    return lt
print(boba(a))
