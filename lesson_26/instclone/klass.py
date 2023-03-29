import requests
from random import randint
class Person:


    def __init__(self,imya="", falimia="", login="", parol=""):
        self.__data = requests.get("https://api.randomdatatools.ru/").json()
        self.__lorem="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris tempor dictum quam, ut tincidunt purus vestibulum sed. Proin mattis hendrerit pharetra. Cras fermentum est magna, ac congue enim bibendum in. Curabitur luctus fermentum lacus, ac laoreet augue tempus a. Sed tempus vulputate ornare. Phasellus accumsan volutpat urna sed pretium. Mauris."
        self.imya = self.__data['FirstName'] if not imya else imya
        #  имя = случайному если атрибут =""(пустое if not) иначе передаваем
        self.falimia = self.__data['LastName']if not falimia else falimia
        self.login = self.__data['Login']if not login else login
        self.__parol = self.__data['FirstName']if not parol else parol
        self.podpiski = []
        self.podpiskishiki = []
        self.posts = [self.__lorem[randint(1,20):randint(20,40)] for i in range(1, 10)]

    def log_in(self, parol, login):
        if self.login == login and self.__parol == parol:
            return True
        else:
            return False