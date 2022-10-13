#familia = input("Фамилия: ").capitalize()
#imya = input("Имя: ").capitalize()
#otchestvo = input("Отчество: ").capitalize()
#
#print(familia, imya [0] + ".", otchestvo[0] + ".")
#print(f"{familia} {imya[0]}. {otchestvo[0]}.")wor
#word = input("Введи фразочку или слово: ")
#print("а", word.count("а"))


#phrase = input("Введите фразу разделённую пробелами: ").strip()
#lst = phrase.split(" ")
#print(lst)
#lst.remove("антона")  #удалить по значению
#print(lst)

#phrase = input("Введи фразу: ")
#find = input("Что меняем: ")
#replace = input("На что меняем: ")
#
#print(phrase.replace(find, replace ))
# replace() - замена первого элемента на второй
#x = input()
#print(x.replace("ё", "йо"
alphabet = {
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "g",
    "д":  "d",
    "е": "e",
    "ё": "yo",
    "ж": "zh"
}

phrase = input("Введи фразу: ")
translate = ""
for bukva in phrase:
    translate = translate + alphabet[bukva]
print(translate)
