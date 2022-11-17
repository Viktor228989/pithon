# lst = [0, 1, 2, 3, 4, 5, 6]
#
# for mega_anton in lst:
#     print(mega_anton)
#
# for super_anton in range(0, 11): # от нуля до десяти включительно
#     print(super_anton)

# x1 = int(input("Число: "))
# x2 = int(input("Число: "))
#
# while x1 <= x2:
#     print(x1)
#     x1 += 1 # то же самое, что и x1 = x1 + 1

# x1 = int(input("Число: "))
# x2 = int(input("Число: "))
#
# for igor in range(x1, x2 + 1):
#     print(igor)

while True:
    try:
        level = int(input("Ярусов: "))
    except ValueError:    # букву в число
        print("Хочу число")
        continue  # перезапустить while
    else: # если ошибок нет
        break  #Вход из while True

while True:
    char = input("Символ: ")
    if len(char) == 1:
        break

for i in range(1, level + 1): # 0-(leve-1) (level раз)
    # левая половина
    print(" " * (level -i), end="")
    print(char * i, end="")

    # правая половина
    print(char * i)
