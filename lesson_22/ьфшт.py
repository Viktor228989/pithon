import json
#
# f = open("data.json", "w", encoding="utf-8")
# text = [False, None, 3, 3.13,(1, 2,3)]
# json.dump(text, f, ensure_ascii=False) # dump - запись в файл
# print(json.dump(text))
# f.close()



# f = open("data.json", "r", encoding="utf-8")
# content =  json.load(f)
# f.close()
# print(content)

# 1 Задача
#
# f = open("file.txt", "r", encoding="utf-8")
# content = f.readlines()
# print(content)
# f.close()
# dame = {}
# for i in (content):
#     k = i.split(':')
#     dame[k[0]] = k[1].rstrip()
# print(dame)
# f = open("data.json", "w", encoding="utf-8")
# json.dump(dame, f, ensure_ascii=False)
# f.close()


# f = open("data.json", "w", encoding="utf-8")
# content = json.load(f)
# f.close()
# print(content)
# for i, elem in enumerate(content):
#     a = type(elem)
#     if a == str:
#         content[i]+="!"
#     elif a in (int, float):
#         content[i]+=1
#     elif a == bool:
#         content[i]=not content
#     elif a == list:
#         print("ghj")
#         content[i]=content[i] + content[i]
#     elif a == dict:
#         # content[i]["newkew"] = None
#     elif a ==None:
#         print("Индекс к удалению:", i)
#         content.pop()

import requests
resp = requests.get(url="http://api.open-notify.org/iss-now.json")
data = resp.json()['iss_position']
print(f"Широта:{data['latitude']} Долгота: {data['longitude']}")

