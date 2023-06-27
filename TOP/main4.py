
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

import copy

def attack():
    print("Включен режим атаки")

Person = {
    "name" : "Варвар",
    "gender" : "Мужской",
    "actions" : {
        "attack" : attack
    }
}


Human = copy.deepcopy(Person)
Human["race"] = "Человек"
Human["skills"] = ["Быстрый бег", "Красноречие"]

Warrion = copy.deepcopy(Human)
Warrion["role"] = "Воин"
Warrion["desk"] = ["Воин отличается своим сочетанием мобильности, живучести,способности..."]

Archer = copy.deepcopy(Human)
Archer["role"] = "Лучник"
Archer["desk"] = ["Лучники способны избегать все эффекты контроля, получать меньше входящего урона..."]
Archer["action"]["attack"] = shoot()


Orc = copy.deepcopy(Person)
Orc["race"] = "Орк"
Orc["skills"] = ["Сила", "Быстрый бег"]

print("-------")
print(Person)
print("-------")
print(Human)
print("-------")
print(Orc)
print("-------")
print(Warrion)
print("-------")
print(Archer)
print("-------")