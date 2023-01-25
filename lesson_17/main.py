BEANS = 20

p1Name = input("Имя первого игрока: ")
p2Name = input("Имя второго игрока: ")
def change(x):
    global BEANS
    BEANS = BEANS - x


while BEANS >1:
    while True: # бесконечный цикл остановится при нормальном значении
        p1 = int(input(f"{p1Name}, сколько фасоли возьмешь: "))
        if p1 <= 5 and p1 >= 1:
            break
    change(p1)

    if BEANS <= 1:
        print("Победил" f"{p2Name}")

    print(f"Фасолин {BEANS}")

    while True: # бесконечный цикл остановится при нормальном значении
        p2 = int(input(f"{p2Name}, сколько фасоли возьмешь: "))
        if p2 <= 5 and p2 >= 1:
            break

    change(p2)
    if BEANS <= 1:
        print("Победил" f"{p1Name}")
    print(BEANS)