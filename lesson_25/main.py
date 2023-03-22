# class Priv:
#     def nazvanie(self, x):
#         self.u = x #публичный
#         self.__naz = "икс" #приватный
#
# nazvanie = Priv()
# nazvanie.nazvanie("хе")
# print(nazvanie.u)
# print(nazvanie._Priv__naz)
#
# class Class:
#     prosto = True # статический атрибут
#     __prosto_priv = True
#     # статическое => у всех объектов одинаковые
#
#     def __init__(self, x="Кефтеме"):
#         self.prosto1 = False
#         self.__prosto_priv2 = x
# obj = Class()
# print(obj.prosto)
from random import randint

class Human:
    default_name = "Игорь"
    default_age = 53
    def __init__(self, name, age,money,hous):
        self.name=name
        self.age=age
        self.__money = 75_000
        self.__hous = False
    def info(self):
        print(self.__money)
        print(self.__hous)
        print(self.name)
        print(self.age)
    def earn_money(self):
         self.__money=self.__money + 56_000

    def default_info(self):
        print(Human.default_name)
        print(Human.default_age)



obj = Human("Игорь", 53, 75_000, False)
obj.info()
obj.default_info()
class  House:
    def __init__(self,area,price):
        self.__area=area
        self.__price=price
    def final_price(self):
        return  self.__price - self.__price * randint(5,25) / 100
obj=House("Улица ыы", randint(5, 123456789))
print(obj.final_price())

