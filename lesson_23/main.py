class Person:  # объявление класса
    def __init__(self, imya, vozrast):  # метод инициализации
        self.age = vozrast  # Установка значений атрибутов
        self.name = imya

    def __str__(self):
        print("Бархат, кефтеме")
leha = Person

print(leha)
print(leha.age)
print(leha.name)


# class Kefteme:
#     def __getitem__(self, item):
#         print("Подкрадули кротячьи. Я ставлю тебе", item)
#
# obj = Kefteme()
# obj[2]
# ЗАДАЧА 1
# import  random
# class XCVBN:
#     def __init__(self, age, name, surname, grades):
#         self.age = age
#         self.name = name
#         self.surname = surname
#         self.grades = grades
#         self.sr = sum(grades) / len(grades)
#     def __str__(self):
#         return(f'Я {self.name} {self.surname} {self.age}')
#     def greet(self):
#         return (f'ай сау братка. Я {self.name} {self.surname} {self.age}')
# n = [random.randint(2, 5) for i in range(2, 10)]
# anna = XCVBN(123, 'аня', 'старперка', [random.randint(2, 5) for i in range(2, 10)])
# anna1 = XCVBN(123, 'аня1', 'человек', [random.randint(2, 5) for i in range(2, 10)])
# anna2 = XCVBN(123, 'аня2', 'cлабая', [random.randint(2, 5) for i in range(2, 10)])
# students = [anna, anna1, anna2 ]
# # d = {anna: anna.sr,
# #      anna2:anna1.sr}
# d = {}
# for i in students:
#     d[i.name] = i.sr
# sorted_tuples = sorted(d.items(), key=lambda item: item[1])
# sorted_dict = {k: v for k, v in sorted_tuples}
# print(d)
# print(sorted_dict)


# 3 ЗАДАЧА
#
# class Popoint:
#     def __init__(self, x, y):
#         self.x=x
#         self.y =y
#     def __str__(self):
#         return f"it is X:{self.x}, It is Y:{self.y}\n"
# class  Rectangle:
#      def __init__(self):
#          self.xyz1 = gg
#          self.xyz2 = ggvp
#      def ploshad(self):
#          a = self.xyz1.x - self.xyz2.x
#          b = self.xyz2.y - self.xyz1.y
#          return a * b
#      def haspoint(self, kok):
#          if (self.xyz2.x <= kok.x <= self.xyz2.x) and (self.xyz2.x <= kok.x <= self.xyz2.x):
#              return True
#          else:
#              return not True
#
#
# gg = Popoint(3456, 154)
# ggvp = Popoint(345, 888888888888888888888888888888)
# barhat = Popoint(123454345543565456567654654567890, 9)
# print(gg, ggvp)
# tp = Rectangle()
# print(tp.ploshad())
# print(tp.haspoint(barhat))

import random
class Wall:
    def __init__(self, width):
        self.width = width
        self.heigest = random.randint(3, 7)

    def print_figure(self):
        d ='''⬛'''
        for i in range(self.heigest):
            print(d * self.width)
obj = Wall(width=10000)
obj.print_figure()

