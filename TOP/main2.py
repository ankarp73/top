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

# 





# ______________________________________________________________________
# **********************************************************************
# [02/06/23]     Massivy   [Spiski]

# genderList = ["Мужской","Женский"]
# print(genderList[0])

# # numberList = [3,1,3,7,9,5,4,2,8,6]
# # numberList.sort()
# # print(len(numberList))


# raceList = ["Человек","Эльф"]
# print(raceList)
# raceList.append("Гном") # Добавим
# print(raceList)



# print(raceList) 
# raceList.pop(1) # удалим
# print(raceList)

# raceList.clear() # очистить весь список


# numberList = [3,1,3,7,9,5,4,2,8,6]
# print(numberList)

# for i in range (0,len(numberList)):
#     # numberList[i] = numberList[i]**2
#     print(i)
#     if numberList(i) % 2 != 0:
#         numberList.pop(i)       
#     print(numberList)


# listN = [[1,2,3,4],
#         [6,7,8,9,10] # двумерный массив
# ]
# print(listN[1][4])


# listN = [[1,2,3,4,5],
#         [6,7,8,9,10],
#         ]
# for i in range(0,len(listN)):
#         print(listN[i])
#         for j in range(0,len(listN[i])):
#                 print([i],[j] , "=", listN[i][j])


genderList = ["Мужской","Женский"]
raceList = ["Человек","Эльф","Гном","Орк","Троль","Огр"]
roleList = ["Воин", "Лучник", "Маг", "Палладин"]

textRace = ""
for i in range(0,len(raceList)):
        textRace += f"{i} - {raceList[i]}\n"

reg_race = False
while reg_race == False:
        myRace = int(input(f"Выберите рассу:\n{textRace}"))
        if myRace > len(raceList) or myRace < 0:
                print("Ошибка. Выберите из перечисленного!")
        else:
                for i in range(0, len(raceList)):
                        if myRace == i:
                                race = raceList[i]
                                reg_race = True
                                print("вы выбрали", myRace)
                                break  # можно без брейка
                        elif myRace == len(raceList):
                                reg_gender = False
                                break

                        
                





