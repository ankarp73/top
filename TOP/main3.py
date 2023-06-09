
#  ПЯТНИЦА  09.06.2023

# productList = ["Каша","Вода"]
# print(productList[0])

# infoProduct = {
#     "nameProduct" : "Каша",
#     "price" : 120,
#     "sale" : "20%",

# }

# print(infoProduct["nameProduct"])
# print(infoProduct["price"])
# print(infoProduct["sale"])

# myName = input("inter yohr name: ")
# myAge = int(input("Введите ваш возраст: "))

# infoPerson = {
#     "namePerson" : "myName",
#     "agePerson" : "myAge",
#     "hobbyPerson" : ["Sport", "Programming", "Booklist"]

# }

# print(infoPerson["hobbyPerson"][0])

#             # list = {
#             #    "key": value]
#             # }

# # for если нужно вывести ключи (перебрать)

# for key in infoPerson:
#     print(f"{key} - {infoPerson[key]}")

# print(f"Имя: {infoPerson["namePerson"]}")  



#_________________________________________________________  
# productList = [
#     {
#         "nameProduct" : "Хлеб",
#         "price" : 55,
#         "count" : 37,
#         "category" : "Выпечка"
#     },
#     {
#         "nameProduct" : "Молоко",
#         "price" : 101,
#         "count" : 20,
#         "category" : "Молочная"
#     },
#         {       
#         "nameProduct" : "Соль",
#         "price" : 18,
#         "count" : 7,
#         "category" : "Соленоё"
#     },
#     {
#         "nameProduct" : "Йогурт",
#         "price" : 105,
#         "count" : 218,
#         "category" : "Молочная"
#     },
#         {
#         "nameProduct" : "Кефир",
#         "price" : 101,
#         "count" : 20,
#         "category" : "Молочная"
#     },
# ]
# for i in range(0,len(productList)):
#     if productList[i]["category"] == "Молочная":
#         productList[i]["price"] = productList[i]["price"] * 2
#         print(f" Название товара - {productList[i]['nameProduct']}")
#         print(productList[i]["price"])
#         print(productList[i]["count"])
#         print("-----------")

# _______________________________________________________________________________

guestList = []
while True:
    nameGuest = input("Введите имя гостя: ")
    ageGuest = int(input("Введите возраст гостя :"))
    # Выше созданные переменные будут появляться в объект infoGuest
    # и вставляться в сооттветствующие ключи
    # infoGuest хранит данные в гостя
    infoGuest = {
        "nameGuest" : nameGuest,
        "ageGuest" : ageGuest,
    }
    # print(infoGuest)
    guestList.append(infoGuest)
    if len (guestList) > 3:
        break

# print(guestList)

for i in range(0,len(guestList)):
    print(f"Имя гостя - {guestList[i]['nameGuest']}")
    print(f"Возраст гостя - {guestList[i]['ageGuest']}")
    print("---------")

# ________________________________________________________________________________

