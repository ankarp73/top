# print(2+5)

# a=2 # int
# print(a, type(a)) # int

# a=str(a) #str
# print(a, type(a))

# z=input("Введите число - мы умножим на 2: ")  # str
# z=int(z) # из строки сделали число
# print(z*2)

# print("Введите информацию о себе")
# my_name=input("Ввелите имя: ")

# print("Информация о пользователе")
# print("Имя:", my_name)

# my_age=input("Введите ваш возраст: ")
# print("My_age:", my_age)

# my_number=input("Введите ваш номер сотового телефона: ")
# print('my_number:', my_number)

# my_height=input("Ваш рост: ")
# weight=input("Ваш вес: ")

# print("height:", my_height)
# print("weight:", weight)

# print("привет" + " " + myName)
# print(f"привет {2+2}")
# print("привет"," ","мир!")


# x = int(input("введите число: ")) #26
# print(x/2)

# # используем // и %
# print(x//10)
# print(x%10)
# a = 2
# b = 2
# h = a / b * 10

# print(int(h))
# print(type(h))

# x = 891 
# a = x
# a1 = x // 100
# print(a1)
# a2 = x // 10 % 10
# print(a2)
# a3 = x % 10
# print(a3)
# print(a1+a2+a3)

# a = 5
# b =10
# # print(a>b)
# # print(a<b)
# if a < b or b > 10: #
#     print("if Выполнилось")

# else:
#     print("Выполнился else")

# login = input("Введите логин")
# password = input("Введите пароль")
# if login == "admin":
#     if password == "admin":
#         print("Вход выполнен")
#     else:
#         print("Неверный логин и пароль: 2 этап")
# else:
#     print("Неверный логин и пароль: 1 этап")



# 5 вопросов, если user score=3: спросит, хочет ли он ответить на доп вопрос.
# Если отв да или yes то задаем ... иначе завершим игру и выдаем ему кол-во очков. 

# q1 = input("Зимой и летом одним цветом: ")
# score = 0
# if q1 == "ёлка" or q1 == "елка" or q1 == "ель":
#     print("Ответ верный!")
#     score = score + 1
#     print(f"score = {score}")
# else:
#     print("Ответ неверный!")
    
    
# q2 = input("Сколько пальцев на руке?: ")
# if q2 == "пять" or q2 == "5":
#     print("ОК. верно")
#     score = score + 1
#     print(f"score = {score}")

# else:
#     print("неправильно!")

# q3 = input("Посадили зёрнышко — Вырастили солнышко.: ")
# if q3 == "подсолнух" or q3 == "Подсолнух":
#     print("ОК. верно")
#     score = score + 1
#     print(f"score = {score}")

# else:
#     print("неправильно!")

# q4 = input("Не огонь, а жжётся: ")
# if q4 == "крапива" or q4 == "Крапива" and q4 == "Лампочка" or "лампочка":
#     print("ОК. верно")
#     score = score + 1
#     print(f"score = {score}")

# else:
#     print("неправильно!")

# q5 = input("Усатая рыба: ")
# if q5 == "Сом" or q5 == "сом" and q5 == "Карп" or q5 == "карп":
#     print("ОК. верно")
#     score = score + 1
#     print(f"score = {score}")

# else:
#     print("неправильно!") 
 
# if score == 5:
#     print('YOU WIN!')
# else:
#     print('Вы не набрали 5 очков, испытание не пройдено')



# x = int(input("Введите число для проверки")) 
# if x % 2 == 0:  
#     print("число чётное")  
# else:
#     print("нечётное") 
# 


x = int(input("Введите число: ")) 
x1 = int(input("Введите число: "))

f = int(input("1-сумма; 2-разность; 3-среднеарифм.; 4-произв."))
if f == 1:
    print(x+x1)
elif f == 2:
    print(x-x1)
    print(x1-x)
elif f == 3:
    print((x+x1)/2)
elif f == 4:
    print(x1*x)
else:
    print("(_!_)")     





