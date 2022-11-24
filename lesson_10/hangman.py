import random


print(art.intro)

vocabulary = ['Anton', 'Alex', 'Alexandr', 'Arsalan', 'Danil', 'Kirill', 'Sergey', 'Nikolay', 'Nasty', 'Natasha', 'Ivan', 'Igor', 'Gosha', 'Galina', 'Olya', 'Oksana', 'Oleg', 'James', 'Bill']
word_answer = random.choice(vocabulary)
word_display = []

for _ in range(len(word_answer)):
    word_display.append("_")

print(word_display)
life = 6
counter = 0

letter_is_be = False

while life > 0 and counter != len(word_answer):
    letter = input("Буква: ").lower()
    for i in range(len(word_answer)):
        if letter == word_answer[i]:
            if word_display[i] != "_":
                letter_is_be= True
            else: # если буква не ушадана
                word_display[i] = letter # переворачиваем букву
                counter += 1
                letter_is_be = True
    if letter_is_be == False:
        life -=1
    print(word_display)

if counter == len(word_answer):
    print("Победа")
else:
    print("Проиграл")
    print(word_answer)