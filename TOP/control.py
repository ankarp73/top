# # 1:
# myCard = input("Введите Ваше: ФИО, возраст, год рождения: ")
# print(myCard)


# # 2:
# print("Загадка. Сидит дед в сто шуб одет, кто его раздевает - тот и слёзы пролтвает. Выберите ответ из следующих вариантов")
# print('1-капуста, 2-лук, 3-чеснок')
# otvet = int(input("Ваш ответ:  "))
# if otvet == 1:
#     print("-неверно, попробуй ещё")
# elif otvet == 2:
#     print("-да, верно, конечно, это лук")
# elif otvet == 3:
#     print("-неверно, попробуй ещё")
# else:
#     print('-ой... что-то пошло не так...')


# # 3:
# from random import randint

# num = int(input("Введите цифру от 1 до 10:  ")) 
# start = int(input("Введите начальный интервальный диапазон числа: "))
# end = int(input("Введите конечный интервальный диапазон поиска числа: "))

# choise = randint(start, end)
# print(f"загаданное число PC: {choise}")

# while True:
#     if num > choise:
#         print("-число меньше")
#     elif num < choise:
#         print("-число больше")
#     elif choise == num:
#         print(f"Верно!")
#         break
#     num = int(input("Заново введите цифру от 1 до 10:  "))
    