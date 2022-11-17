import random

is_game = "y"
while is_game == "y":
    card = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    hand_player = [random.choice(card)]
    hand_computer = [random.choice(card)]
    score_player = 0
    score_computer = 0
    get_card = "y"
    while get_card == "y":
        hand_player.append(random.choice(card))
        if sum(hand_player) > 21 and 11 in hand_player:  # если > 21 и туз в руке
            for i in range(0, len(hand_player)): # перебираем карты
                if hand_player[i] == 11: # ищем туза
                    hand_player[i] = 1 # меняем 11 на 1
                    break # только до первого туза

        score_player = sum(hand_player)
        print(f"Твоя рука: {hand_player}. Очков: {score_player}")
        print(f"Первая карта компьютера: {hand_computer[0]}")

        if score_player > 21:
            get_card = "n"
        else:
            get_card = input("Берем карту? y - да, n - нет")
    while sum(hand_computer) < 17:
        hand_computer.append(random.choice(card))
        if sum(hand_computer) > 21 and 11 in hand_computer:  # если > 21 и туз в руке
            for i in range(0, len(hand_computer)):  # перебираем карты
                if hand_computer[i] == 11:  # ищем туза
                    hand_computer[i] = 1  # меняем 11 на 1
                    break  # только до первого туза
    score_computer = sum(hand_computer)
    print("=" * 10)
    print(f"Твоя рука: {hand_player}. Очков: {score_player}.")
    print(f"Рука компа: {hand_computer}. Очков: {score_computer}.")

    #  кто победил?
    if score_player > 21 and score_computer > 21:
        print("Ничья")
    elif score_computer > 21:
        print("Пабеда")
    elif score_player > 21:
        print("Проиграл")
    elif score_player == score_computer:
        print("Ничья")
    elif score_player > score_computer:
        print("Победа")
    else: #comp = player
        print("Проиграл")

    is_game = input("Играем дальше? y = да n = нет")
