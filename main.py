# Задачи на циклы и оператор условия------
# ----------------------------------------
import numpy as np

'''
Задача 1

Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
# for i in range(1, 6):
# print("No "+str(i) + ". " + "0" * 1001)


'''
Задача 2

Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''

'''case = "Введите по очереди 10 цифр: "
print(case)
counter = 0
for i in range(10):
    number = int(input(str(i + 1) + ')'))
    if number == 5:
        counter += 1
print('Количество введеных пользователем цифр 5 = ', counter)'''

'''

Задача 3

Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''

'''count = 1
for i in range(1, 101):
    count += i
    print(count)'''

'''
Задача 4

Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''

'''count = 1
for i in range(1, 11):
    count *= i
    print(count)'''

'''
Задача 5

Вывести цифры числа на каждой строчке.
'''

number = input('Введите число: ')
list_number = list(number)
list_number.reverse()
rev_number = int("".join(list_number))

while rev_number > 0:
    print(rev_number % 10)
    rev_number //= 10

'''
Задача 6

Найти сумму цифр числа.
'''
num = int(input('Enter a number: '))


'''
Задача 7

Найти произведение цифр числа.
'''

'''
Задача 8

Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
integer_number = 213413
while integer_number > 0:
    if integer_number % 10 == 5:
        print('Yes')
        break
    integer_number = integer_number // 10
else:
    print('No')

'''
Задача 9

Найти максимальную цифру в числе
'''

'''
Задача 10

Найти количество цифр 5 в числе
'''
