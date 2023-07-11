
# *****************_________+++ Вторник  27.06.2023  "Функции" +++_________*********************

# Делигирование









# # двиг и его функции
# def start():
#     print("Запуск")

# def stop():
#     print("Стоп")

# Engine = {
#     "start" : start,
#     "stop" : stop,
# }

# Engine["start"]()
# Engine["stop"]()

# def open():
#     print("Капот открыт")

# def close():
#     print("Капот закрыт")

# Bonnet = {
#     "open" : open,
#     "close" : close,
# }

# # основа авто
# Car = {
#     "color" : "",
#     "marka" : "",
#     "Engine" : "",
#     "Bonnet" : "",

# }

# auto = Car
# auto["marka"] = "audi"
# auto["color"] = "green"
# # print(auto)
# auto["Engine"]["start"]()



# Mash = {
#     "color" : "",
#     "marka" : "",
# }

# Car = Mash.copy
# Car["Engine"] = Engine
# Car["Doors"] = "двери"

# myAuto = Car
# myAuto["color"] = "Синий"



# основная функция

# def Car(marka,color,engine):
#     thisMarka = marka
#     thisColor = color
#     thisEngine = engine

#     activelist = {
#         "showMarka" : showMarka
#     }
    

# def showMarka(param):
#     print(param)


# auto = Car("audi","green",Engine)
# auto

# _____________________________________________________

# import copy

# def attack():
#     print("Включен режим атаки")

# Person = {
#     "name" : "Варвар",
#     "gender" : "Мужской",
#     "actions" : {
#         "attack" : attack
#     }
# }


# Human = copy.deepcopy(Person)
# Human["race"] = "Человек"
# Human["skills"] = ["Быстрый бег", "Красноречие"]

# Warrion = copy.deepcopy(Human)
# Warrion["role"] = "Воин"
# Warrion["desk"] = ["Воин отличается своим сочетанием мобильности, живучести,способности..."]

# Archer = copy.deepcopy(Human)
# Archer["role"] = "Лучник"
# Archer["desk"] = ["Лучники способны избегать все эффекты контроля, получать меньше входящего урона..."]
# Archer["action"]["attack"] = shoot()


# Orc = copy.deepcopy(Person)
# Orc["race"] = "Орк"
# Orc["skills"] = ["Сила", "Быстрый бег"]

# print("-------")
# print(Person)
# print("-------")
# print(Human)
# print("-------")
# print(Orc)
# print("-------")
# print(Warrion)
# print("-------")
# print(Archer)
# print("-------")

# *********************************************************************************************************
# _______________________________________ Четверг 29.06.2023 ______________________________________________
# _____________________________________________ class _____________________________________________________
# *********************************************************************************************************


# class Car:
#     def __init__(self, color, marka, motor):
#         self.color = color
#         self.marka = marka
#         self.motor = motor


#     # методы - действия с определённым классом
#     def showColor(self):
#         print(self.color)

#     def showMarka(self):
#         print(self.marka)


# class Engine:
#     def __init__(self, HP, volume):
#         self.HP = HP
#         self.volume = volume

#     def start(self):
#         print("Запуск")

#     def stop(self):
#         print("Стоп")


# class Conditioner:
#     def __Conditioner__(self, cooling):
#         self.cooling = cooling


# myEngine = Engine(120, 2)
# twoEngine = Engine(280,2.2)
# myAuto = Car("green", "audi", myEngine)

# myAuto.motor.start()


# class Wheel:
#     def __init__(self, marka, seasonality, radius, profile):
#         self.marka = marka
#         self.seasonality =seasonality
#         self.radius =radius
#         self.profile =profile

#     def turn_left(self):
#         print("Повернуть налево")

#     def turn_right(self):
#         print("Повернуть на право")

#     def take_off(self):
#         print("Снять колесо")

#     def put_on(self):
#         print("Надеть колесо")


# # class Light:
# #     def __init__(self, type, voltage, plinth)

# print(myAuto.motor.volume)



#  # Наследование
# # class EngineSport()

# twoEngine = Engine(500,2)

# class SportCar(Car):
#     def __init__(self, color, marka, motor,turbo):
#         self.turbo = turbo
#         super().__init__(color, marka, motor)

# lamborginiEngine = Engine(900, 6)
# twoAuto = SportCar("blue","lamborgini", twoEngine, True)

# twoAuto.showMarka()




# from abc import ABC, abstractclassmethod

# class Animal(ABC):
#     def __init__(self, name, sound):
#         self.name = name
#         self.sound = sound

#     def activeSound(self):
#         print(self.sound)

# class Cat(Animal):
#     def __init__(self, name):
#         super().__init__(name, "Мяу")

#     def purr(self):
#         print("Мурлыкает")            

# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name, "Гав")

#     def digHole(self):
#         print("Копает яму")

# myCat = Cat("Вася")
# myCat.purr()
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

# 4 июля урок (абстрактный метод)

# class Bird():
#     def __init__(self, name, sound):
#         self.name = name
#         self.sound = sound

#     def eat(self):
#         print("Ест")

#     def hunting(self):
#         print("Охотятся")

#     def activeSound(self):
#         print(self.sound)

# class noFly(Bird):
#     def __init__(self, name, sound=""):
#         super().__init__(name, sound)
    
#     def goes(self):
#         print("Летает")

# class Fly(noFly):
#     def __init__(self, name, sound=""):
#         super().__init__(name, sound)

#     def noFly(self):
#         print("Летает")

# class Crow(Fly):
#     def __init__(self, name, sound=""):
#         super().__init__(name, "-Кар-кар!!!")

# crow = Crow("Гриша")
# crow.activeSound()


























# 21 - 07 августа каникулы
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~    Tuestoday~Вторник 11.07.2023  ~~~~~~~~~~~~~~~~~~~~~~~

# хранит просто инф
base_list = [
        {
        "first_name" : "Денис",
        "last_name" : "Кириллов",
        "birthday" : "01.06.2001",
        "gender" : "мужской",
        "login" : "denis161",
        "password" : "12345",
    },
        {
        "first_name" : "Антон",
        "last_name" : "Карпов",
        "birthday" : "02.07.2011",
        "gender" : "мужской",
        "login" : "anton162",
        "password" : "12346",
    },
        {
        "first_name" : "Анастасия",
        "last_name" : "Капустина",
        "birthday" : "03.08.2012",
        "gender" : "женский",
        "login" : "настя163",
        "password" : "12347",
    },
        {
        "first_name" : "Вераника",
        "last_name" : "Мастина",
        "birthday" : "04.09.2013",
        "gender" : "женский",
        "login" : "верон164",
        "password" : "12348",
    },
        {
        "first_name" : "Вася",
        "last_name" : "Пупкин",
        "birthday" : "11.09.2015",
        "gender" : "мужской",
        "login" : "вася165",
        "password" : "12348",
    },
]

register_users = [


]

class User():
    def __init__(self, user_id, first_name, last_name, birthday, gender, login,
                password):
                self.user_id = user_id
                self.first_name = first_name
                self.last_name = last_name
                self.birthday = birthday
                self.gender = gender
                self.login = login
                self.password = password
                # ~~~~~~~~~~~~~~~~~~~~~~~
                self.status = "user"
                self.blocking = False

    # Если в классе есть методы с словом update,значит, этот метод для изм инф

    def update_first_name(self, new_first_name):
        self.first_name = new_first_name

    def update_last_name(self, new_last_name):
        self.last_name = new_last_name

    def update_birthday(self, new_birthday):
        self.birthday = new_birthday

    def update_gender(self, new_gender):
        self.gender = new_gender

    def update_password(self, new_password):
        if self.password == input("Введите старый пароль:  "):
            self.password = new_password

class Moderator(User):
    def __init__(self, user_id, first_name, last_name, birthday, gender, login,
    password):
        self.status = "moderator"
        super().__init__(user_id, first_name, last_name, birthday, gender, login,
        password )

    def blocking_user(self, users_list):
        """для блокировки пользователя"""
        text_user_list = f"id | first_name | blocking | status \n"
        for i in range(0, len(users_list)):
            text_user_list += f"{i} - {users_list[i].user_id}{users_list[i]['first_name']} - {users_list[i]['blocking']} {users_list[i]['status']}\n"
        print(text_user_list)
        input_user_id = int(input("Введите id пользователя для блокировки: "))
        for i in range(0,len(users_list)):
            if self.status == "moderator":
                if input_user_id == i and users_list[i]['status'] != "moderator" and users_list[i]['status']!= "admin":
                    if users_list[i]['blocking'] == True:
                        print("пользователь уже заблоктрован")
                        break
                    else:
                        users_list[i]['blocking'] = True
                        print("пользователь успешно заблокирован")
                        break

class Admin(Moderator):
    def __init__(self, user_id, first_name, last_name, birthday, gender, login, password):
        super().__init__(user_id, first_name, last_name, birthday, gender, login, password)
        self.status = "admin"
    def delete_user_list(self, user_list):
        user_list.clear()
        print("База данных удалена")
                            # massiv - явл массивом данных
    def create_user_list(self, massiv, user_list):
        for i in range(len(user_list),len(massiv)):
            user_list.append(User(user_id=i,
                                first_name=massiv[i]["first_name"],
                                last_name=massiv[i]["last_name"],
                                birthday=massiv[i]["birthday"],
                                gender=massiv[i]["gender"],
                                login=massiv[i]["login"],
                                password=massiv[i]["password"]))

class Registration():
    def __init__(self) -> None:
        pass
    def create_user(self, users_list):
        users_list.append(User(len(users_list),
                                input("введите имя: "),
                                input("введите фамилию: "),
                                input("введите дату рожд: "),
                                input("введите пол: "),
                                input("введите логин: "),
                                input("введите пароль: ")))

class InLog():
    def __init__(self, login, password):
        self.login = login
        self.password = password
    def log_in_account(self, users_list):
        for i in range(len(users_list)):
            if users_list[i].login == self.login and users_list[i].password == self.password:
                print("вход выполнен")
                break
            else:
                print("Ошибка")

class Manager():
    def __init__(self, reg, inlog, userModerAdmin, datalist):
        self.reg = reg
        self.userModerAdmin = userModerAdmin
        self.datalist = datalist
    def work(self):
        print(self)


my_reg = Registration
my_inlog = InLog
my_person_list = [User(),Moderator(),Admin()]        
my_base = []
myManager = Manager(my_reg, my_inlog, my_person_list, my_base)
myManager.userModerAdmin[0](10,"admin","admin","01.01.01","муж","admin","admin")
myManager.inlog("admin","admin")








# class Manager(Registration,InLog):
#     def __init__(self) :
#         super().__init__()





# proverka = Registration()
# proverka.create_user()
                                                  
# myAdmin = Admin(10,"admin","admin","01.01.1970","Мужской","admin","admin")
# myAdmin.create_user_list(base_list, register_users)

# myLogin = InLog(input("Введ логин: "), input("Введ пароль: "))
# myLogin.log_in_account()






# print(register_users[0])
# print(register_users[1].first_name)
# register_users[0].update_first_name("Danila")
# print(register_users[0].first_name)

# continie
# primer = [
#     User(0,"name","last.name","01.06.2001","Мужской","login","pass"),
#     User(0,"name","last.name","01.06.2001","Мужской","login","pass"),
# ]










