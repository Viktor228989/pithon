from pictures import box_carrot, box_empty, box_close
from random import choice

def generate_boxes(status1, status2):
    result = ""
    if status1 == "ПУСТОТА":
        box1 = box_empty.format(COLOR1.center(13)).split("\n")
    elif status1 == "МОРКОВКА":
        box1 = box_carrot.format(COLOR1.center(13)).split("\n")
    else:
         box1 = box_close.format(COLOR1.center(13)).split("\n")


    if status2 == "ПУСТОТА":
        box2 = box_empty.format(COLOR2.center(13)).split("\n")
    elif status2 == "МОРКОВКА":
        box2 = box_carrot.format(COLOR2.center(13)).split("\n")
    else:
         box2 = box_close.format(COLOR2.center(13)).split("\n")

    for element in zip(box1, box2):
        result += "   ".join(element) + "\n"
    result += p1Name[:10].center(13) + " " * 7 + p1Name[:10].center(13) + "\n"
    return result


COLORS = ["ФИОЛЕТОВАЯ", 'КАЙФОВАЯ', 'МАГАДАНСКАЯ','МОСКОВСКАЯ']
COLOR1 = choice(COLORS)
COLOR2 = choice(COLORS)
while COLOR1 == COLOR2: # чтобы было()цвета разные
    COLOR2 = choice(COLORS)

p1Box = "Закрыто"
p2Box = "Морковка"









p1Name = input(">>> Имя первого пользователя: ")
while p1Name.strip() == "": # Если убрав пробелы останется пустота
    p1Name = input(">>> Имя первого пользователя: ")

p2Name = input(">>> Имя второго пользователя: ")
while p1Name.strip() == "":
    p2Name = input(">>> Имя второго пользователя: ")

print(generate_boxes("ПУСТОТА", "мох"))

while True:
    print(f"{p2Name}, в твоей коробке {p2Box}")

# блеф/правда
    action = input(f"Нужно сделать выбор:\n"
                   f"1. Блеф: сказать что в коробке {p1Box}"
                    f"2. Правда: сказать что в коробке {p2Box}"
                   f">>> (Б - блеф, П - правда) -> ").upper()
    while action != "Б" and action != "П":
        action = input(f">>> (Б - блеф, П - правда) -> ").upper()

    print("\n" * 70)
    input(f">>> {p1Name} открывает глаза(Enter)...")
    if action == "Б":
        print(f"{p2Name} сообщает, что в его коробке {p1Box}")
    else:
        print(f"{p2Name} сообщает, что в его коробке {p2Box}")