# def add_one(a, b):
#     return a + b + 1
#
# add_one2 = lambda a, b: a + b + 1 # аналогичная лямбда функция
#
#
# result = lambda answer: True if answer == "Д" else False # if-else нутри lamda
#
#
# # list comprehension
# from random import randint
# lst =[]
# for i in range(5):
#     lst.append(randint(1, 5))
# print(lst)
#
# lst2 =[for n in range(6)]
# # list comprehension всегда пишется в []
# # 2. for n in range() - обычный цмкл for -> сколько элементов будет в списке
# # 3. Перед for -> сам добавляемый элемент
# print(lst2)

# первая задача
# c2f = lambda c: 9/5 * c + 32
# print(c2f(200))
#
# f2c = lambda f: (f - 32) * 5/9
# print(f2c(200))
#
# c2k = lambda c: c + 273.15
# k2c = lambda k: k - 273.15
# f2c = lambda f: c2k(f2c(f))
# degree = 203
# print(f2c(degree))
#
# from random import randint
#
# exit_code = lambda vihod: True if vihod == "Д" else False
# while True:
#     k = int(input("Сколько кубиков бросаем?"))
#     lst2 = [randint(1, 6) for n in range(k)]
#     print(lst2)
#     if exit_code (input("Выходим?"))
#         break

# задача 3
# from random import choice
#
#
# chars = [list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"),
#          list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя"),
#          list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
#          list("abcdefghijklmnopqrstuvwxyz"),
#          list("1234567890")
#         ]
# a = "https://www.google.com"
# dict = {}
# f = [choice(choice(chars)) for i in range(6)]
# b = ''.join(f)
# print(b)
# if a in dict:
#     print('ок', dict[a])
# else:
#     dict[a] = b
#     print("сслке по кайфу", dict[a])



# 4 задача

field = {"A": ["⬜", "⬜", "⬜"],
         "B": ["⬜", "⬜", "⬜"],
         "C": ["⬜", "⬜", "⬜"]}

cell_letter = ["A", "B", "C"]
cell_number = ["1", "2", "3"]
def drawer()-> None:
    """отрисовывает поле три на три"""
    print("1 2 3")
    for row in range(3):
        print(cell_letter[row], end="")
        for column in range(3):
            print(list(field.values())[row][column],end="")
        print()

def turne(player) -> None:
    """ход игрока"""


print(drawer)