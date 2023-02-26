# x = input("Введи имя друга: ")
# try:
#     if x == "Антон":
#          raise NameError("Ахахаххахахахаххахахахаххахахахахахахахахахахахахахахахаххахаахахахахахахахахаххахахахахахахахахахаахахахахахахахахахахахахахаххахахахаахаххахахахаххахаххахахахахахахахахахахахахахахаахахахахахахахаххахахах🉐")
# except NameError as pelmeni:
#     print("Низя.", pelmeni)




# 1 Задача
# def skladivanie():
#     s = 0
#     k = 0
#     for number in content:
#         try:
#            s += int(number)
#         except ValueError:
#             print("Найдено не число:", number)
#         else:
#              k += 1
#         if k == 0:
#             return "Где числа?"
#     return round(s / k, 2)
#
#
#
# try:
#     f = open("file.txt", "r", encoding="utf-8")
# except FileNotFoundError:
#      print("Файла нет")
#      exit()
# content = f.read().split()
# print(content)
#
# print("Ср. арифм =", skladivanie())

# Задача 2
try:
   f = open("file.txt", "r", encoding="utf-8")
except FileNotFoundError:
    print("Файла нет")
    exit()
content = f.readlines()
if content == []:
     print("Файл пустой")
     quit()
print(content)

for i, student in enumerate(content):
    content[i] = student.split()

print(content)

maxi = -1
imya = ""
familiya = ""
for student in content:
    try:
         if int(student[3]) > maxi:
          maxi = int(student[3])
          imya = student[1]
          familiya = student[0]
    except ValueError:
        print("Баллы отсутствуют:", student)
    except IndexError:
         print("Баллы осутствуют:", student)

print(imya, familiya,maxi)



