# # ЦИКЛЫ
# # while (пока)
# x = 10
# while x != 0: # (пока x не равен нулю)
#     print(x)
#     x -= 1 # то же саммое, что и x - 1
#
# while True: # срабатывать каждый раз
#     break # выйти из цикла

# for
# lst = ["А", "Б", "В", "Г", "Д"]
# for letter in lst: # проитерироваться по списку
#     print(letter)
#
# for i in range(0, 3):
#     print(i)


# word = input("Введи словечко: ")
# while word: # пока слово не пустое
#     print(word, end=" ")
#     word = word[:-1]

#
# x = int(input("Введи число: "))
# while x != 0: # while x: (из-за типа "число")
#     if x % 2 == 0:
#         print(x)
#     x -= 1  # то же самое, что и x = x - 1


x = input("Введи число: ")
if not x.isdigit() or int(x)  <= 1:  # если не числовое значение
    print("Одна ошибка и ты ошибся")
    quit()
else:
    x = int(x)

step = 0
while x != 1:
    step += 1 # то же самое что и step = step + 1
    if x % 2 == 0:
        print(f"{step})", end=" ")
        print(x, "/ 2 =", end=" ")
        x = x // 2
    else:
        print(f"{step})", end=" ")
        print(x, "/ 2 =", end=" ")
        x = x * 3 + 1
    print(x)
print("Шагов: ", step)