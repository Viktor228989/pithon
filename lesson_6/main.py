# x = 7
# if x == 5: # Я не сработаю
#    print("Я не сработаю")
# elif x > 5:
#    print("x > 5")
# else: # если не сработает if или elif
#    print("Я, вероятно сработаю😃")

# word_1 = input("Введи слово (1/2): ")
# word_2 = input("Введи слово (2/2): ")
#
# word_1 = word_1.lower()
# word_2 = word_2.lower()
#
# if word_1.isalpha() and word_2.isalpha():
#
#     sorted_w1 = sorted(word_1)
#     sorted_w2 = sorted(word_2)
#
#     print(sorted_w1)
#     print(sorted_w2)
#
#     if sorted_w1 == sorted_w2:
#         print("Ура, у вас анаграмма")
#     else:
#         print("Ну не получилось")
#
# else:
#     print("Хочу только буквы")

q1 = input("Сколько будет 2 + 2?\n"
           "а) 4, б) 5\n"
           "--> ")
if q1 == "а":
    print("Правильно")
else:
    print("Одна ошbбка и ты проиграл")
    quit()

q2 = input("Арбуз - это(с ботанической точки зрения)..?\n"
           "а) корнеплод, б) овощ, в) ягода\n"
           "-->")
if q2 == "в":
    print("Правильно")
else:
    print("Одна ошbбка и ты проиграл")
    quit()
q3 = input("Что такое цукцванг?\n"
           "а)положение в шашках и шахматах, в котором любой ход игрока ведёт к ухудшению его позиции. ,\n"
           "б)sırt çantası\n"
           "в) поджанр аниме посвящённый Егору \n"
           "г) порода обезьяны\n"
           "--> ")
if q1 == "a":
    print("Правильно")
elif q3 == "в":
    print("Ты гений")
else:
    print("Одна ошибка и ты проиграл")
    quit()

print("Ты победил")


