# class FiftiFifti:
#     def __init__(self):  # магическое
#         self.__zarplata = 20_000  # private
#
#     def ipotek(self):
#         if self.__zarplata > 75_000:  # ИСПОЛЬЗОВАНИЕ ПРИВАТНЫХ ДАННЫХ
#             return True
#         else:
#             return False
#
#     def povishenie(self):  # public метод
#         self.__zarplata += 30_000
#
#     def __bar(self):  # private метод
#         return True
#
#     def gou(self):
#         if self.__zarplata > 1:
#             print(self.__bar())
#
#
# sanya = FiftiFifti()
# # sanya._FiftiFifti__zarplata = 21_000  # private
# # print(sanya._FiftiFifti__zarplata)
#
# sanya.gou()

# 1 задача
# class Car:
#     def __init__(self):
#         self.status = 0
#
#     def start(self):
#         if self.status == 1:
#             print("Я уже")
#         else:
#             print("Завёлся")
#             self.status = 1
#
#     def stop(self):
#         if self.status == 0:
#             print("Я уже")
#         else:
#             print("Развёлся")
#             self.status = 0
#
#     def y(self, year):
#         self.y = year
#         print(self.y)
#
#     def t(self, type):
#         self.t = type
#         print(self.t)
#
#     def c(self, color):
#         self.c = color
#         print(self.c)
#
# reno = Car()
# reno.c("Черный")
# reno.y("20")
# reno.t("Бэчбэк")
# reno.start()
# reno.start()
# # reno.stop()
# import string
#
# class Alphabet:
#     def __init__(self):
#         self.__alfavit = string.ascii_lowercase
#         self.__lang = "Eng"
#
#     def print(self):
#         print(self.__alfavit)
#
#     def letters_num(self):
#         print(len(self.__alfavit))
#
# alpha = Alphabet()
# alpha.print()
# alpha.letters_num()
# zadacha 3
# import datetime
# class Clocks:
#     def __init__(self):
#         self.__time = '23:59:59'
#         # self.__time = datetime.datetime.now().strftime("%H:%M:%S")
#         self.__h, self.__m, self.__s = self.__time.split(":")
#         self.__h, self.__m, self.__s = int(self.__h), int(self.__m), int(self.__s)
#     def __test_h(self):
#         if self.__h >= 24:
#             self.__h = 0
#     def __test_m(self):
#         if self.__m >= 60:
#             self.__m = 0
#             self.__h += 1
#
#     def __test_s(self):
#         if self.__s >= 60:
#             self.__s = 0
#             self.__m += 1
#     def hour(self):
#         self.__h = int(self.__h)+1
#         self.__test_h()
#     def min(self):
#         self.__m = int(self.__m) + 1
#         self.__test_m()
#         self.__test_h()
#     def sec(self):
#         self.__s = int(self.__s) + 1
#         self.__test_s()
#         self.__test_m()
#         self.__test_h()
#     def coc(self):
#         return f'{str(self.__h).rjust(2, "0")}:{str(self.__m).rjust(2, "0")}:{str(self.__s).rjust(2, "0")}'
# c = Clocks()
# c.sec()
# c.hour()
# c.min()
# print(c.coc())

from random import choice


class Blablabla:
    def __init__(self):
        self.__counter = 5

    def increment(self):
        self.__counter += 1

    def decrement(self):
        self.__counter -= 1

    def ret(self):
        return self.__counter


counter = Blablabla()
l = [counter.increment, counter.decrement]  # сохраняем возможные объекты

while 0 < counter.ret() < 10:
    choice(l)()  # выбор объекта + вызов
    print(counter.ret())