"""
Задание 1
Дана переменная, в которой хранится слово из латинских букв. Напишите код, который выводит на экран:

    среднюю букву, если число букв в слове нечетное;
    две средних буквы, если число букв четное.
"""

my_word = 'дезоксирибонуклеиновая'
if len(my_word) % 2 != 0:
    print(my_word[len(my_word) // 2])
else:
    print((my_word[len(my_word) // 2 - 1]), my_word[len(my_word) // 2], sep="")

"""
==============================================================================================
Задание 2
Напишите программу, которая последовательно запрашивает у пользователя числа (по одному за раз) и после первого нуля выводит сумму всех ранее введенных чисел.
"""
sum = 0
number = int(input("Введите число: "))
while number != 0:
    sum += number
    number = int(input("Введите число: "))
print("Результат: ", sum)


"""
==============================================================================================
Задание 3
Мы делаем MVP dating-сервиса, и у нас есть список парней и девушек.
Выдвигаем гипотезу: лучшие рекомендации мы получим, если просто отсортируем имена по алфавиту и познакомим людей с одинаковыми индексами после сортировки! 
Но мы не будем никого знакомить, если кто-то может остаться без пары:
"""

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys) == len(girls):
    print("Идеальные пары:")
    for el in range(0, len(boys)):
        print(sorted(boys)[el], "и", sorted(girls)[el])
else:
    print("Внимание, кто-то может остаться без пары!")

"""
============================================================================================
Задание 4
У нас есть список, содержащий информацию о среднедневной температуре в Фаренгейтах за произвольный период по странам (структура данных в примере).
Необходимо написать код, который рассчитает среднюю температуру за период в Цельсиях(!) для каждой страны.
"""
countries_temperature = [
['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
['Germany', [57.2, 55.4, 59, 59, 53.6]],
['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]

print('Средняя температура в странах:')
for el in range(0, len(countries_temperature)):
    avg_temperature = sum(countries_temperature[el][1]) / len(countries_temperature[el][1])
    print(countries_temperature[el][0], '-', round((avg_temperature - 32) / 1.8, 1), "C")

