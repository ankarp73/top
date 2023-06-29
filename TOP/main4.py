
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






class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def activeSound(self):
        print(self.sound)

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Мяу")

    def purr(self):
        print("Мурлыкает")            

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Гав")

    def digHole(self):
        print("Копает яму")

myCat = Cat("Вася")
myCat.purr()

