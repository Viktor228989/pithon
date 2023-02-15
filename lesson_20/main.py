# f = open("восьмой бэ дежурный класс.txt", "w", encoding="UTF-8")
# f.write("Ноль\nОдин")
# f.close()

# f = open("восьмой бэ дежурный класс.txt", "r", encoding="UTF-8")
# # t = f.read()
# t1 = f.readlines()
#
# print(t1)
# for line in t1:
#     print(line.rstrip()) # rstrip() - убирает пустоты справа

# 1 задача
#
# a = input("Введи название файла: ")
# f = open(a, "w", encoding="UTF-8")
# b = input("Введи фразу: ")
# f.write(b)
# print("файл записан")
# while b != '':
#     f.write(b)
#     b = input("введи")
#     print()
# f.close()

# Задача 2

# a = input('введи название: ')
# f = open(a, 'r', encoding='utf-8')
# b = f.readlines()
# f.close()
# print(b)
# f = open(a, 'w', encoding='utf-8')
# n = 0
# print(b)
# for line in b:
#     n += 1
#     f.write(f'{n}) {line}')

# Задача 3

# f = open('tadjik artem.txt', "r", encoding='utf-8')
# b = f.readlines()
# print(b)
# n = 0
# while b != []:  # пока список не пустой
#     d = b[:3] # зафиксировали три элемента
#     del b[:3]
#     stas = open(f'{n}.txt', 'w', encoding='utf-8')
#     for i in d:
#         stas.write(i)
#     stas.close()
#     n += 1

# Задача 4

a = open("file.txt", "r", encoding="utf-8")
fylesi = a.readlines
print(fylesi)

chislo = int(input("Пчем пицца: "))
result = fylesi[-chislo:]
print(result)
