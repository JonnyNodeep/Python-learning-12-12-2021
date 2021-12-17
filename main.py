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

'''number = input('Введите число: ')
list_number = list(number)
list_number.reverse()
rev_number = int("".join(list_number))

while rev_number > 0:
    print(rev_number % 10)
    rev_number //= 10'''

'''
Задача 6

Найти сумму цифр числа.
'''
'''num = int(input('Enter a number: '))
sum = 0
while num > 0:
    sum += num % 10
    num //= 10
    print(sum)'''

'''
Задача 7

Найти произведение цифр числа.
'''
'''num = int(input('Enter a number: '))
mult = 1
while num > 0:
    mult *= num % 10
    num //= 10
    print(mult)'''

'''
Задача 8

Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
'''int_num = int(input('Enter a number: '))
while int_num > 0:
    if int_num % 10 == 5:
        print('5 is hear')
        break
    int_num //= 10
else:
    print('5 is absent')'''

'''
Задача 9

Найти максимальную цифру в числе
'''
# first variant

# int_num = list(input('Enter a number:'))
# max_numb = max(int_num)
# print(max_numb)

# second variant

int_num = 23456
max_num = int_num % 10
int_num = int_num // 10

while int_num > 0:
    if int_num % 10 > max_num:
        max_num = int_num % 10
    int_num = int_num // 10
print(max_num)



'''
Задача 10

Найти количество цифр 5 в числе
'''
'''int_number = 21555555413
count = 0
while int_number > 0:
    if int_number % 10 == 5:
        count += 1
    int_number = int_number // 10

    print(count)'''

