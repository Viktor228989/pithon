from klass import Person
from random import choice
def ofor():
    u = choice(users)
    print(f"Логин: {u.login}")
    print(f"Имя: {u.imya}")
    print(f"Фамилия: {u.falimia}")
    print(f"Посты: {u.posts}")


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
            continue

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
        session()


print(c.imya)