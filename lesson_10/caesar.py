alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = [" ", ".", ",", "-", "(", ")", "?", "!"]
should_end = False

while should_end == False:
    text = input("Сообщение: ").lower()
    text = list(text) # строку -> в список
    print(text)

    shift = int(input("Сдвиг: "))

    if shift > len(alphabet): # > 26
        shift = shift % len(alphabet)
    elif shift < -len(alphabet): # < - 26
        shift = shift % -len(alphabet)

    # механизм сдвига
    cipher_text = ""
    for letter in  text:
        if letter == " ": # если спец. символ
            cipher_text += letter # запись без изменений
        else:
            position = alphabet.index(letter)
            if position + shift > len(alphabet):
                new_position = position + shift - len(alphabet)
            elif position + shift < 0:
                new_position = position + shift + len(alphabet)
            else:
                new_position = position + shift
            cipher_text += alphabet[new_position]
    print(cipher_text)