#  ZeroDivisionError
#  x = 5/0
#
#
#
#  TypeError
#  x = "a" + 15
#
#
#
#  IndexError
#  x = [0, -15, "Антон"]
#  x [3]
#
#
#
#  SyntaxError
#  x = "Привет, я Антон.
#
#  SyntaxError
#  if 5 == 4
#     print()
#
#
#
#  NameError
#  x = "Я строчка"
#  print(x2)
#
#
#
#  assert --> AssertionError
# def summa(numbers):
#     return sum(numbers)
#
#  print(summa([3,4]))
#
# assert summa([1,2]) == 3
# assert summa([1,2]) == 4
# try - попытаться
# except - отлавливание исключений
#try:
 #   number = int(input())
#    x = 5 / 0
#except ZeroDivisionError:
 #   print("На ноль делить нельзя")
#except ValueError:
#    print("Хочу цифирки")
#except Exception:  # Любая ошибка будет обработана
#    print("Ты ошибся")
#else:  # else - когда все хорошо
#    print("Я поделил")
#finally:
#    print("Здесь был я")
# pass
# try:
#     number = int(input())
#     x = 5 / number
# except Exception:
#     pass # Затычка. Нечего не произойдет
#if 5 == 5:
#    pass # TODO: купить молока и дописат код

try:
    x = input("Введи имя:")
    if x == "Антон":
        raise Exception("Антона в обиду не дам")
    #raise - Вызвать исключение, ощибку
except Exception as  error_message:
    # as - сохранить ошибку в error_message
    print("Это слово запрещено!")
