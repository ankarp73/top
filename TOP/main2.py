# myName = "anton"

# start = int(input("Введите начальное значение: "))
# end = int(input("Введите конечное значение: "))

# for i in range(start,end+1):
#     print(i)

# for i in myName:
#     print(i)
#     if i == "o":
#         break

# x = int(input("Введите число на проверку: "))
# for i in range(2,x+1):
#     if x % i == 0 and x != i:
#         print("Число сложное")
#         break
#     elif i == x:
#         print("Число простое")



#  Вывод чисел, которые кратные 2 и 7:
# for x in range(0,100):
#     if x % 2 == 0 and x % 7 == 0:
#         print(x)



# Вывести таблицу умножения:

# x = int(input("Ввести цифру: "))
# for i in range(2,10):
#     print(f"{x}*{i} = {x*i}")


#  Вывести сумму для определенного диапазона:




# sum=0
# for i in range(5,8):
#     sum = sum+i
#     print(sum)


# i=0
# b=10
# while i < 10 and b > 0:
#     print(i)
#     print(b)
#     i = i + 1
#     b = b - 3 


# i=0
# b=10
# while i != 11 and i < 100:
#     print(i)
#     i = i + 2 


# i=0
# b=10
# while True:
#     print(12)
#     i = i + 1
#     if i > 10:
#         break

# myName = "anton"
# print(len(myName))
# i = 0
# while i < len(myName):



# f = int(input("Введите факториал: "))
# for i in range(1,f):
#     f = f*i
#     print(f)



# 30 мая среда

# import time
# for h in range(0,24): # i=1
#     for m in range(0,60): # j=1
#             for s in range(,60):
#                 print(f'ч:{h}м:{m}с:{s}')
#                 time.sleep(1/10)



# import time
# h=0
# m=0
# s=0

# while h < 24:
#     m=0
#     while m < 60:
#         s=0
#         while s < 60:
#                 print(f'ч:{h}м:{m}с:{s}')
#                 time.sleep(1/10)
#                 s+=1
#         m+=1
#     h+=1

#_________________________________________________________________

# -_______________*********dz10*************______________________:

# dd = int(input("d"))
# mm = int(input("m"))
# yy = int(input("y"))

# if mm == 4 or mm ==6 or mm == 9 or mm==11:
#     if dd >=30:
#         mm+=1
#         dd=1
#         print(dd,mm,yy)
#     elif dd < 30:
#         dd+=1
#         print(dd,mm,yy)
#     elif mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10:
#         if dd >=31:
#         mm+=1
#         dd=1
#         print(dd,mm,yy)

        #......
        











# ___________________________________________________________________

# использование циклов внутри циклов, возврат значений, +условия

print("Регистрация персонажа")
reg = False
while reg == False:
    reg_gender = False
    while reg_gender < False:
        gender = (input("Выберете пол персонажа \n1-муж\n2-жен\nВвод>>>: "))
        if gender == "1":
            gender = "Мужской"
            reg_gender=True
        elif gender == "2":
            gender = "Женский"
            reg_gender=True
        else:
            print("Ошибка.Выберите из перечисленного!")

    reg+=1
    if reg_gender == 1:
        reg_race = 0
        while reg_race < 1:
            race = input("Выберите рассу персонажа \n1-Человек\n2-Эльф\nВвод>>>: ")
            if race == "1":
                race == "Человек"
                reg_race+=1
            elif race == "2":
                race = "Эльф"
                reg_race+=1 
            elif race == "0":
                reg_race+=0
                break
            else:
                print("Ошибка. Выберите из перечисленнного")
            if reg_race == 1:
                reg_role = 0
                if race =="Человек":
                    while reg_role == 0:
                        role = input("0<-назад Выберите рассу персонажа \n1-Воин\n2-Лучник\nВвод>>>: ")
                        if role == "1":
                            reg_role == 1

                elif race == "Эльф": 
                    pass   
reg+=1  