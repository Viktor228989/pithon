# Первый задача
# phrase = "Россия, Россия, Россия и Богдан! ".title().strip()
# print(phrase)
# symbols = list("!@#$%^&*()1234567890'\",.?") # \" - экранирование.
# phrase_clear = "" # щас будем мыть фразу
# for ovoshi in phrase: # итерирова ься по фразе
#     if ovoshi not in symbols: # если это не спец. символ
#         phrase_clear += ovoshi
#
# phrase_list = phrase_clear.split(" ")
# print(phrase_list)
#
# d = {}
# for dom in phrase_list:
#     if dom not in d: # если ключа нет
#         d[dom] = 1 # обозначение нового элемента {"Россия": 1}
#     else: # если ключ есть
#         d[dom] += 1 # плюс один
# print(d)

# Второй задача
# sloj = 0
# d = {"Молоко":100,
#      "Доширак": 21,
#      "Чипсы": 0.5,
#      "Богдан": 999}
#
# for i in d.values():  # перебор по значениям
#    sloj += i
# print(sloj)


# Тритий (за дачей)
die_sides = 6
die_count = 2
d = {}

for first in range(1, die_sides + 1): # от 1 до 6
    for second in range(1, die_sides + 1):
        if first + second not in d:  # если суммы кубиков нет в словаре
            d[first + second] = [(first, second)]
        else: # если такой ключ уже есть
            d[first+second].append((first, second))

# вывод
for tadjikistan in d:
    print(f"{tadjikistan}: {d[tadjikistan]}")