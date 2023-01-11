# def peimeni(spisok:list) -> int: # type hinting
#     """Функция, ктороая показывает кто где падал"""
#     s = 0
#     for element in spisok:
#         s += element
#     return s
#
# # -------------------------------
#
# lst = [5, 4, 6, 2, 1]
# peimeni(lst)
# print(peimeni(lst))
#
# def join(spisok:list, sep:str):
#     result=""
#     for element in spisok:
#         result = element + element + sep
#     return result
#
# lst = ["Я", "очень", "крутой"]
#
# print(join(sep="|", spisok=lst))






# def factorial(chislo:int):
#     result = 1
#     for element in range(2, chislo + 1):
#         result *=element
#     return result
#
#
# print(factorial(chislo=5))

#
# def aye_bassota(stroka:str):
#     mjlj = {"верх": 0,
#             "низ": 0}
#     for i in stroka:
#         if i.isupper():
#             mjlj["верх"] += 1
#         else:
#             mjlj["низ"] += 1
#
# print(aye_bassota(stroka="строка"))