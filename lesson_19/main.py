# import easygui
# alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
# pendos_alphabet = "abcdefghijklmnopqrstuvwxyz"
# pendos_alphabet2 = alphabet[::-1]
# alphabet2 = alphabet[::-1]
#
# y = ""
#
# easygui.enterbox(
#     msg="введи слово",
#     title="жесть",
# )
# for i in x:
#     if i not in alphabet:
#         if i not in pendos_alphabet:
#             y += i
#         else:
#             y += alphabet2[alphabet.index(i)]
# print(y)
# easygui.msgbox(
#     msg=y,
# )











# a =  input("введи что-то...")
# n = int(input("введи сдвиг..."))
# mas = []
# fras = []
# for i in a:
#     fras+=chr(ord(i)+n)
# print(fras)



#
# a = input("uihfuie: ")
# n = int(input("uihfuie: "))
# alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
# fras = ''
# for i in a:
#     c = alphabet.index(i)
#     c = (c+n)%33
#     fras+=alphabet[c]
# print(fras)

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя".upper()
fras = 'ЫНУЪЫ, УЧЫЧЩДТ ЮЧЫНФЧЪЕ ЙД АЫЧЙД ЩИРЛИМИФС'
contr_slov = "ТЕКСТ"
fraser = ''
for i in fras:
    if i in alphabet or i == "":
        fraser+=i
    mas = fraser.split(" ")
    for shift in range(1,33):
        ghf = ''
        for letter in contr_slov:
            c = alphabet.index(letter)
            c = (c+shift)%33
            ghf+=alphabet[c]
        if ghf in mas:
            print("Сдвиг равен:",shift)
            quit()

