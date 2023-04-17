# Все задания оборачиваются в функции






# Задание 1:
# У вас есть идея создать Back-end для игры: "Угадай число."
# Данный код генерирует рандомное число.
###################
# import random as rd
# random_number = rd.randint(0,10)
# print(random_number)
###################
# С помощью функции:
#    my_number = int(input("Введите число: "))
# спрашивайте число от пользователя.
# Запустите бесконечный цикл!
# И пытайтесь спрашивать у пользователя какое-то число каждый раз.
# Если пользователь угадал число которое сгенерировал компьютер остановите цикл и скажите пользователю - "Вы угадали!"
# Если пользователь не угадал вы снова спросите у него число.
# Если пользователь 3 раза подряд не угадал число, вы останавливаете цикл и говорите: "Вы проиграли..."
#######################################################################



# Задание 2:
        # Напишите программу, которая циклично запрашивает у пользователя номера символов по таблице Unicode и выводит соответствующие им символы. 
        # Завершает работу при вводе нуля.
###################################################################



# Задание 3:
        # Напишите программу, которая измеряет длину введенной строки. 
        # Если строка длиннее десяти символов, то выносится предупреждение. 
        # Если короче, то к строке добавляется столько символов *, чтобы ее длина составляла десять символов, после чего новая строка должна выводиться на экран.
###################################################################



# Задание 4:
        # Напишите программу, которая запрашивает у пользователя шесть вещественных чисел. 
        # На экран выводит минимальное и максимальное из них, округленные до двух знаков после запятой. 
        # Выполните задание без использования встроенных функций min() и max().
####################################################################



# Задание 5:
        # Напишите программу которая принимает число любой длины и вытаскивает из него самое большое и самое маленькое число.
####################################################################



text = """
The Zen of Python, by Tim PetersBeautiful is better than ugly.Explicit is better than implicit.
Simple is better than complex.Complex is better than complicated.
Flat is better than nested.Sparse is better than dense.
Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.
Errors should never pass silently.Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one--and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea --let's do more of those!
"""
################################################################




# Задание 6:
#     Функция
#     Напишите функцию, которая берет текст, и возвращает строковое значение, состоящее из заглавных букв. 
#     Используйте текст, данный выше (The Zen of Python).
#     Подсказка: используйте метод строчных значений, который проверяет, “заглавность” буквы.
##################################################################





# Задание 7:
#     Чтение из файла.
#     Создайте файл с текстом The Zen of Python. 
#     Напишите функцию, которая считайте его и возвратит список из слов, которые начинаются на букву “c” или “C”.
#     Подсказка: используйте метод строчных значений, который проверяет, начинается ли слово на переданную букву.
####################################################################




# Задание 8:
#     Банкомат
#     Напишите код банкомата, который принимает цифру, выдает деньги с номиналом 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 3, 1.
#     Подсказка: напишите функцию, используйте divmod()
##################################################################





# Задание 9:
#     Напишите функцию которая принимает два аргумента (числа), умножает их друг на друга, 
#         и возвращает функцию, которая также берет два аргумента (числа), 
#             и возвращает результат умножения аргументов внешней функции плюс результат деления 
#                 аргументов внутренней функции.
#     Подсказка: (outer_arg1 * outer_arg2) + (inner_arg1 / inner_arg2)
####################################################################





# Задание 10:
#     Фильтрация с помощью filter(). Необходимо написать функцию, и передать ее filter(), 
#     чтобы получить список только тех слов из текста text (см. выше “The Zen of Python”), что содержат букву ‘p’.
#     Подсказка: необходимо заменить \n на пробел. 

#     То есть, это нужно проделать еще до фильтрации. 
#     Функция, которая будет передана в filter() должна возвращать True, если в слове есть буква ‘p’.
#####################################################################




# Задание 11:
#     Дано
    # dict_one = {'a':1, 'b':2, 'c':3}
    # dict_two = {'d':4, 'e':5, 'f':6}
    # dict_three = {'g':7, 'h':8, 'i':9}
    # dict_four = {}
#     С помощью цикла for необходимо собрать три первых словаря в словарь dict_four

#     Подсказка: Для удобства итерации, первые три словаря можно записать в кортеж (dict_one, dict_two, dict_three
#####################################################################




# Задание 12:
#     Аналог шифра цезаря ". Программа должна запрашивать элементы
#     списка через пробел. После чего пользователь должен ввести значение
#     для сдвига элементов списка. Значение может быть как положительным,
#     так и отрицательным. Если значение положительное, элементы списка
#     должны сдвигаться вправо, если отрицательное - влево. Результат
#     необходимо вывести на экран:

#     Пример:
#     [1, 2, 3, 4, 5], сдвиг 2
#     [3, 4, 5, 1, 2]
#####################################################################





# Задание 13:
#     Напишите программу, где исходный список содержит положительные и отрицательные числа. 
#     Требуется положительные поместить в один список, а отрицательные - в другой.
###################################################################




# Задание 14:
#     Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).
#####################################################################




