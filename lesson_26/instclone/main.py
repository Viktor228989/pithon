from klass import Person
from random import choice
def ofor():

    print(f"Логин: {u.login}")
    print(f"Имя: {u.imya}")
    print(f"Фамилия: {u.falimia}")
    print(f"Посты: {u.posts}")

def select_user():
    # global u
    # u = choice(users)
    # while True:
    #     if u.login == current.login: # если выбрали сами себя
    #         u = choice(users)
    #     else:
    #         break

     global u
     while True:
        u = choice(users)
        if u.login != current.login:
            break
def session():
    while True:
        ofor()
        print('''[Возможные действия]: 
    - ПОДПИСКИ (посмотреть на кого подписан Ибрагим)
    - ПОДПИСЧИКИ (посмотреть кто подписан на Ибрагима)
    - ПОДПИСАТЬСЯ (стать подписчиком)
    - СЛЕДУЮЩИЙ аккаунт''')
        spros = input('>').upper()
        if spros == 'Выйти':
            break
        elif spros == 'сЛЕДУЮЩИЙ':
            select_user()
        elif spros == 'Подписаться':
            current.podpiskishiki +=1
            u.podpiskishiki += 1


a = Person("Чек")
b = Person('степан', 'кревесенко', 'yalox', 'jora')
c = Person()
users=[a,b,c]
print(ofor())
print(a.imya)
l = input('скажи логин: ')
p = input("скажи пароль: ")

for i in users:
    if i.log_in(login=l, parol=p) == True:
        current = i
        session()
print(c.imya)
