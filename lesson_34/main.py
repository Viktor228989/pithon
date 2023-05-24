slovar = {"key1": "value1",
          "key2": "value2",
          "key3": "value3",
          "key4": "value4",
          "key5": "value5"}
# 1 способ=================
# print(slovar.keys())
# print(slovar.values())
# ============================
keys = []
values = []
for i in slovar:
    values.append(slovar[i])
    keys.append(i)
print(values)
print(keys)


