# doneЗадание №1:

# Если взять ВСЕ числа от 0 до 10, которые деляться на 3 или 5 БЕЗ ОСТАТКА, то получим 3, 5, 6 и 9.
# Сумма этих чисел равна 23 (3+5+6+9) = 23.

# Найдите сумму всех чисел меньше 1000, кратных 3 или 5.

# a = [i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0]
# print(sum(a))


######################################## 1
#done







# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# doneЗадание №2:
# a = 333
# b = 555
# a, b = b, a
# print('a =', a)
# print('b =', b)

######################################## 1

# Поменяйте значения переменных местами(НЕ ВРУЧНУЮ!), чтобы в ПЕРЕМЕННОЙ "a" было значение 555, а в ПЕРМЕННОЙ "b" было значение 333.
 #done

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# doneЗадание №3:
# Если взять строку - "237" и сложить все её числа то получится 2+3+7 = 12.
# Возьмите строку "4729461084" и сложите все её числа.
# Результат выведите на экран.

# number = '4729461084'
# number_1 = list(map(int, number.strip()))
# print(number_1)
# print(sum(number_1))

######################################## 1

#done

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# doneЗадание №4:
# Создайте input() который принимает от пользователя дату в формате: "2020-10-24 18:30" и возвращает dictionary разделённую по значениям даты:
# menu['drinks'] = ['Coca-Cola', 'Sprite', 'Fanta']
# date = {}
# date['year'] = [int(input('enter full year'))]
# date['month'] = [int(input('enter month (numerical)'))]
# date['day'] = [int(input('enter day'))]
# date['time'] = [input('enter exact time (time:minutes)')]
# print(date.values())


#done


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# NE ZNAUЗадание №5:
# Какое слово нужно сложить 5 раз чтобы получить число 5?
# Какое слово нужно умножить на 7 чтобы получить 7?
 #NE ZNAU
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# ===========================================================                2                     ===============================================================================


# doneЗадача 1
# Есть список: # # Выведите все элементы, которые больше 5.
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in a:
#     if i > 5:
#         print(i)

######################################## 1

#done

# Задача 2
# Есть набор чисел # Поделить каждое число из digits на 9 и вывести на экран.
# digits = (113,118,-5,1,135,137,0,142,144,17,154,0,155,2,159,172)
# for i in digits:
#     print(i/9)

######################################## 1

#done


# doneЗадача 3
# Здесь замешаны разные типы данных.
# Напишите программу, которая берёт массив данных spisok2 и выводит только те элементы из spisok_2, которых нет в spisok_1.
# spisok_1 = ('Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23)
# spisok_2 = ('Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23)
# a = set(spisok_2)
# b = set(spisok_1)
# b.difference_update(a)
# print(b)

######################################## 1

#done
# ========================================================                3                     ===============================================================================


# doneЗадание 1:
# Напишите программу, которая выводит чётные числа из списка длиною 300 объектов
#    и останавливается, если встречает число 237.

# number = 300
# for i in range(0, 300):
#     if i == 237:
#         break;
#     elif i % 2 == 0:
#         print(i)

######################################## 1

#done

# Задание 2:
# 1. Спросите у пользователя предложение и поделите его по пробелам.
# Если пользователь ввёл меньше шести слов спросите снова, Не принимайте предложения если оно короче 6 символов, спрашивайте снова и снова.
# 2. Поделите полученный лист на 2 равные части (Если число элементов листа нечетное, то длина первой части должна быть на один жлемент больше)
# 3. Переставьте эти две части местами и запишите в лист.

# a = 'Простот слова из шести букв навкрное возможно'
#
# sentences = a.split(' ')
# if len(sentences) > 6:
#     print('Дааа слов больше 6')
#
# while True:
#     a = input('please enter a sentence, put comma after each word: ')
#     n = list(a)
#     if i in range(0, len(a)):
#         if a[i] < 6:
#             print('please enter again: ')
#     else:
#         print('thank you')


# doneЗадание 3:
# Вам дан список:# Определите количество четных и не четных.
# numbers = [2,4,7,1,8.4,-3.3,7.1,-2,4,-1,7,-43,8,-3,6,9]
# #
# even = 0
# odd = 0
# for i in numbers:
#     if i % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print(even, odd)

######################################## 1
#done


# doneЗадание 4:
# Дан список  целых чисел:
#
# Создайте новый лист и замените отрицательные числа на -1, положительные на число 1, ноль оставить без изменения.

# numbers = [0,2,4,7,1,8,0,-3,7,0,-2,4,0,0,-1,7,-43,0,8,-3,6,9]
# numbers_2 = []
#
# for i in numbers:
#     if i < 0:
#         numbers_2.append(-1)
#     elif i > 0:
#         numbers_2.append(1)
#     else:
#         numbers_2.append(0)
#         print(numbers_2)

######################################## 1
#done

# doneЗадание 5: # Выведите все элементы списка с четными ИНДЕКСАМИ (то есть A[0], A[2], A[4], ... ])
# my_list = [2,4,6,8,10,1,3,5,7,9,11,13,17]
# for i in my_list:
#     if i % 2 == 0:
#         print(i)
#done

# doneЗадание 6:
# Дан список чисел:

# Выведите все элементы списка, которые больше предущего элемента
# Пример: (numbers: 1,5,2,4,3 Результат: 5,4)

# numbers = [1,0,-2,4,3,6,6,3,5,8,4,2]
# for i in range(0, len(numbers)):
#     if numbers[i] > numbers[i-1]:
#         print(numbers[i])

######################################## 1
#done

# doneЗадание 1:
# Нужно создать обычный калькулятор состоящий из знаков +,-,*,/
# 1. У пользователя просят выбрать знак
# 2. Просят ввести 1-ое число
# 3. Просят ввести 2-ое число
# 4. Вывести результат
# 5. После результата спросить у пользователя хочет он закончить или нет,
# если нет то калькулятор должен запускатся сначала
# 6. Учесть то что деление на ноль невозможно


#
# while True:
#     sign = input('please choose the sign +,-,*,/   ')
#     if sign in ('+', '-', '*', '/'):
#         first_number = float(input('please enter the first number'))
#         second_number = float(input('please enter the second number'))
#     if sign == '+':
#         print(first_number + second_number)
#     elif sign == '-':
#         print(first_number - second_number)
#     elif sign == '*':
#         print(first_number * second_number)
#     elif sign == '/':
#         if second_number != 0:
#             print(first_number / second_number)
#         else:
#             print('на ноль делить нельзя')
#
#     ask = input('want to repeat?' )
#     if ask == 'no':
#         print('bye')
#         break
#     else:
#         print('start again ')


######################################## 1

#done

################################################################################


# done Задание 2:
# Даны три переменные "A", "B" и "C".
# Изменить значения этих переменных так, чтобы в "A" хранилось значение "A"+"B",
# в "B" хранилась разность старых значений "C" - "A",
# а в "C" хранилось сумма старых значений "A" + "B" + "C".
# Например, A=0, B=2, C=5, тогда новые значения A=2, B=5 и C=7.

# a = int(input())
# b = int(input())
# c = int(input())
# A = a + b
# B = c - b
# C = a + b + c
# print('новые значения:', 'A=', A , 'B=', B , 'C=', C )

######################################## 1
#done
################################################################################


# doneЗадание 3:
# Пользователь вводит сторону квадрата. Найдите периметр и площадь квадрата.
# a = int(input())
# S = a*2
# P = 4*S
#
# print(S, P)
# print(a * 4)
# print(a * a)
#done
################################################################################


# !Задание 4:
# Вам даны несколько последовательностей чисел:
# sequence_0 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0)
# sequence_2 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0.0)
# sequence_3 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70')


# Нужно проверить, все ли числа в КАЖДОЙ последовательности уникальны.
# Если в последовательности были найдены дубликаты ---> Выведите на экран: "Последовательность не уникальна."
# Если в последовательности дубликатов найдено не было ---> Выведите на экран: "Последовательность уникальна."
# Если в решении задания не присутствует цикл ---> Задание не защитано.

# sequence_0 = (14, 10, 35, 45, '60', 70, 90, 0, 105, 150, 10.0, 45.0, '70', 0)
# sequence_2 = (14, 10, 35, 45, '60', 70, 90, 0, 105, 150, 10.0, 45.0, '70', 0.0)
# sequence_3 = (14, 10, 35, 45, '60', 70, 90, 0, 105, 150, 10.0, 45.0, '70')
#
# if len(set(sequence_0)) == len(sequence_0):
#     print("Последовательность 0 уникальна.")
# else:
#     print("Последовательность 0 не уникальна.")
#
# if len(set(sequence_2)) == len(sequence_2):
#     print("Последовательность 2 уникальна.")
# else:
#     print("Последовательность 2 не уникальна.")
#
# if len(set(sequence_3)) == len(sequence_3):
#     print("Последовательность 3 уникальна.")
# else:
#     print("Последовательность 3 не уникальна.")
################################################################################


# doneЗадание 5:
# Создайте input и спросите у пользоваетля как работает встроенная функция reversed().
# В терминале пользователя должен ввести пример функции reversed() и отправить это вашей программе.
# Ваша программа должна исполнить ту часть кода которую ввёл пользователь и вывести на экран результат.
# Если пользователь ввёл что-то не по синтаксису Python поймайте это с помощью try: except:
# Если пользователь всё ввёл верно выполните его программу.
# Если поймали ошибку ---> Спросите снова как работает встроенная функция reversed().


# guess = input('как работает встроенная функция reversed() - ')
# rev = 'возвращает обратный итератор'
# while guess != rev:
#     print('try again')
#     guess = input('как работает встроенная функция reversed() - ')
# else:
#     print('true')

#done


################################################################################


# doneЗадание 6:
#     Дано четырехзначное число. Верно ли, что цифры в нем расположены по убыванию?
#     Например, 4311 - нет, 4321 - да, 5542 - нет, 5631 - нет, 9871 - да.
# a = int(input('четырехзначное число - '))
# pervoe_chislo = a//1000
# vtoroe_chislo = a%1000//100
# tretie_chislo = a%1000%100//10
# chetvertoe_chislo = a%1000%10
# if pervoe_chislo > vtoroe_chislo and vtoroe_chislo >  tretie_chislo and tretie_chislo > chetvertoe_chislo:
#     print('da')
# else:
#     print('net')

#done
################################# 1


################################# 13

