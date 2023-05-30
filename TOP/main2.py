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



f = int(input("Введите факториал: "))
for i in range(1,f):
    f = f*i
    print(f)
