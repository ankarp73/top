
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

# guestList = []
# while True:
#     nameGuest = input("Введите имя гостя: ")
#     ageGuest = int(input("Введите возраст гостя :"))
#     # Выше созданные переменные будут появляться в объект infoGuest
#     # и вставляться в сооттветствующие ключи
#     # infoGuest хранит данные в гостя
#     infoGuest = {
#         "nameGuest" : nameGuest,
#         "ageGuest" : ageGuest,
#     }
#     # print(infoGuest)
#     guestList.append(infoGuest)
#     if len (guestList) > 3:
#         break

# # print(guestList)

# for i in range(0,len(guestList)):
#     print(f"Имя гостя - {guestList[i]['nameGuest']}")
#     print(f"Возраст гостя - {guestList[i]['ageGuest']}")
#     print("---------")

# # ________________________________________________________________________________





#  13 июня   Вторник  Была контрольная 5 заданий
#  
#  ------------------------------------------------------------------------------
#  ------------------------------------------------------------------------------
#
#  16 июня   Пятница Знакомство с функциями

# numEnt = int(input("загадайте число\n от 0 до 100: "))
# print("Каждая итерация будет ровно делиться частями,\nт.е. с каждой последующей итерацией диапазон будет делиться пополам.")

# -----------------------------------------


# def reg(x):

#     print(x)

# reg(input("Введите своё имя: "))

#  ------------------------------------------------------------------------

# def regName(myName):
#     print(myName)

# def regGender():
#     listGender = ["муж","жен"]
#     textGender = ""
#     for i in range(0,len(listGender)):
#         textGender += f"{i} - {listGender[i]}\n"
#     # print(textGender)
#     myGender = int(input(f"{textGender}\n:"))
#     for i in range(0,len(listGender)):
#         if myGender == i:
#             myGender = listGender[i]
#             break

# def globalReg():
#     print("Рег персонажа")
#     x = int(input("Выбор действия: \n1-Ввод имени>\n2-Выбор Гендера>\n:"))
#     if x == 1:
#         regName(input("Имя: "))
#     elif x == 2:
#         regGender()

# globalReg()

# def regRace():
#     pass
#  --------------------------------------------------------------------------


# def regName(myName):
#     print(myName)
    
# def regRace():
#     listRace = ['Человек','Эльф','Гном','Орк','Троль','Гоблин',]
#     textRace = ""
#     for i in range(0,len(listRace)):
#         textRace += f"{i} - {listRace[i]}\n"
#     # print(textRace)
#     myRace = int(input(f"{textRace}\n:"))
#     for i in range(0,len(listRace)):
#         if myRace == i:
#             myRace = listRace[i]
#             break
#     print(f"Ты выбрал: {myRace}")
#     # globalReg()

# def globalReg():
#     print("Рег персонажа")
#     x = int(input("Выбор действия: \n1-Ввод имени>\n2-Выбор Race>\n:"))
#     if x == 1:
#         regName(input("Имя: "))
#     elif x == 2:
#         regRace()

# globalReg()

#  -------------------------------------------------------------------------------
#  -------------------------------------------------------------------------------

#  20.06.23 Вторник тема: Функции и возврат значений.



# def f1(a):
#     c = a - 50
#     print(f'экран: ваша сдача: {c}')
#     return c

# ## f1(200) = 150
# #print(f"Вы получили на руки {f1(200)}")
# f1(200)





# myInfo = {

# }

#                     # print(myInfo)
#                     # myInfo["myName"] = "Denis"
#                     # print(myInfo)

#             # myInfo
# def regName(massiv, newName):
# #   myInfo["myName"] = newName    
#     massiv["myName"] = newName
#     return massiv


# def regGender(massiv):
#     regName(massiv, input("Ваше имя: "))


# def globalreg(massiv):
#     x = int(input("1-м\n2-ж\n"))
#     if x == 1:
#         massiv["myGender"] = "м"
#     elif x == 2:
#         massiv["myGender"] = "ж"
#     return massiv


# newInfo = globalReg(myInfo)
# print(newInfo)

#  ________________________________________________

# num1 = int(input("Введите 1-ое число: "))
# num2 = int(input("Введите 2-ое число: "))
# num3 = int(input("Введите 3-ое число: "))
# choice = input("Сумма или произведение чисел:\n1-сумма\n2-произведение\n")
           
# def sum_and_proiz_set(num1, num2, num3):
#     if choice == 1:
#         num1+num2+num3
#         return
#     elif choice == 2:
#         num1*num2*num3
#         return


# print(sum_and_proiz_set(num1, num2, num3))

#  _____________________________________________________

#  *************Пятница 23.06.2023 *********

usersLists = []  # список пользователей
[
    {
        "userLogin" : "admin",
        "userPasssword" : "admin",
        "userName" : "Anton",
        "userFirstName" : "Karpov",
    },

    {
        "userLogin" : "admin",
        "userPasssword" : "admin",
        "userName" : "Anton",
        "userFirstName" : "Karpov",
    },

    {
        "userLogin" : "admin",
        "userPasssword" : "admin",
        "userName" : "Anton",
        "userFirstName" : "Karpov",
    },
]  # пример хранения данных
userList = []

while True:
    x = int(input("Введите: \n1-Регистрация нового пользователя: \n2-Вход в личный кабинет: \nВвод: "))
    if x == 1:
        print("--Регистрация--")
        while True:
            regUser = {
                "userLogin" : "",
                "userPassword" : "",
                "userName" : "",
                "userFirstName" : "",
            }
            while True:
                regLogin = input("Введите логин: ")  # admin1
                if len(userList) > 0:
                    for i in range(0,len(userList)):
                        if regLogin != userList[i]["userLogin"]:
                            regUser["userLogin"] = regLogin
                        else:
                            print("Данный логин уже занят, введите другой")
                            regUser["userLogin"] = ""
                            break    
                else:
                    regUser["userLogin"] = regLogin
                if len(regUser["userLogin"]) > 0:
                    break
            regUser["userPassword"] = input("Введите пароль нового пользователя: ")
            regUser["userName"] = input("Введите имя нового пользователя: ")
            regUser["userFirstName"] = input("Введите фамилию нового пользователя: ")
            print("Регистрация завершена.\n")
            check = int(input("1-подтвердить\n2-ввести данные снова\nВвод:"))
            if check == 1:
                userList.append(regUser)
                break
            elif check == 2:
                print("--Регистрация--")
    elif x == 2:
        print("--Вход в ЛК")
        inLogin = input("Введ логин: ")
        inPassword = input ("Введ пароль: ")
        for i in range(0,len(userList)):
            if inLogin == userList[i]["userLogin"] and inPassword == userList[i]["userPassword"]:
                print("Вход выполнен")
                while True:
                    infoUser = int(input("1-Просмотр инфо\n2-Редактир инфо\n3-Выход\n"))
                    if infoUser == 1:
                        print(f'Имя : {userList[i]["userName"]}\n',
                                f'Фамилия : {userList[i]["userFirstName"]}\n',
                                f'Логин : {userList[i]["userLogin"]}\n',
                                f'Пароль : {userList[i]["userPassword"]}\n')
                    elif infoUser == 2:
                        print("Редактирование данных")
                        upDate = int(input("1-Имя\n2-Фамилия\n3-Пароль"))
                        if upDate == 1:
                            print("Ваше имя {userList[i][userName]}")
                            userList[i]["userName"] = input("новое имя: ")
                        if upDate == 2:
                            print("Ваша фамилия {userList[i][userFirstName]}")
                            userList[i]["userFirstName"] = input("новая фамилия: ")
                        if upDate == 3:
                            print("Ваш пароль {userList[i][userPassword]}")
                            userList[i]["userPassword"] = input("новый пароль: ")
                    elif infoUser == 3:
                        break
                break
            elif len(userList) - 1 == i:
                print("Неверный логин или пароль")