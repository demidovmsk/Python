
# 1.Посчитать сумму всех введенных чисел:

# a = int(input("введите первое число: "))
# b = int(input("введите второе число: "))
# c = int(input("введите третье число: "))

# print ( "Ответ: ", a + b + c )

# 2. Даны два числа: A, B. Проверьте истинность высказывания: "Числа A и B имеют одинаковую четность".

# a = int(input("введите первое число: "))
# b = int(input("введите второе число: "))

# if a % 2 == b % 2:
#     print("Оба числа четные")
# else:
#     print("Оба числа или одно из чисел нечетные")

# 3. Пользователь вводит два целых числа. Введите меньшее из них.

# a = int(input("введите первое число: "))
# b = int(input("введите второе число: "))

# if a > b:
#     print(a)
# elif a == b:
#     print("числа равны")
# else:
#     print(b)

# 4. Пользователь вводит целое число. Введите "YES", если число 4-значное, "NO" если нет.

# a = int(input("введите первое число: "))

# if a > 999 and a <10000:
#     print ("yes")
# elif a < -999 and a > -10000:
#     print ("yes")
# else:
#     print("No")

# За день машина проезжает n километров. Сколько дней нужно, чтобы она проехала m километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.

# n = int(input("Сколько машина проезжает за день?: "))
# m = int(input("Сколько машина проехала километров?: "))
# print ("Ответ: Данный маршрут машина проехала за", -(-m // n), "дней.")

# или

# print ("Ответ: Данный маршрут машина проехала за", ((n + m -1) // n), "дней.")

# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в каждом из трех классов. Выведите наименьшее число парт, которое нужно приобрести для них.

# a = int(input("Сколько учащихся в 1 классе?: "))
# b = int(input("Сколько учащихся во 2 классе?: "))
# c = int(input("Сколько учащихся во 3 классе?: "))

# # count_desk_a = a // 2 + a % 2
# # count_desk_b = b // 2 + b % 2
# # count_desk_c = c // 2 + c % 2
# # print("Ответ: Для всех учащихся необходимо",count_desk_a + count_desk_b + count_desk_c, "парт.")

# count_desk_a = (a + 1)  // 2
# count_desk_b = (b + 1)  // 2
# count_desk_c = (c + 1)  // 2
# print("Ответ: Для всех учащихся необходимо",count_desk_a + count_desk_b + count_desk_c, "парт.")

# Задача №9. Решение в группах
# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
# Input: 5
# Output: 120

# n = int(input("Введите число: "))
# fact = 1

# # while n > 0:
# #     fact *= n
# #     n -=1

# print(fact)

# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

# n = int(input("Введите число: "))
# n0 = 0
# n1 = 0
# n2 = 1
# i = 2 # Так как 2 первых числа уже известны (0 И 1)
# while n0 < n:
#     n0 = n1 + n2
#     n1 = n2
#     n2 = n0
#     i += 1
#     if n0 > n:
#         i = 0
# if i != 0:
#     print(i)
# else:
#     print(-1)

# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2
# from random import randint
# n = int(input("Введите число: "))
# count = 0

# for i in range(n):
#     t = randint(-10, 50)
#     print(t, end=' , ')
#     if t > 0:
#         count += 1

# print()
# print('Количество теплых дней:', count)

# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.

# Решение: сколько конкретных чисел?

# list_number = [1, 1, 2, 0, -1, 3, 4, 4]
# print(list_number.count(4))

# Решение с использованием for

# list_number = [1, 1, 2, 0, -1, 3, 4, 4]
# count = 0
# for item in list_number:
#     if item%1 == 0:
#         count += 1
#         print("количество элементов, подходящих под данные условия = ", count)

# Решение с использованием len

# list_numbers = [1, 1, 2, 0, -1, 3, 4, 4]
# element_count = len([item for item in list_numbers if item%1 == 0])
# print("количество элементов, подходящих под данные условия = ", element_count)

# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]


# l = list(map(int, input("Введите арифметическую последовательность: ").split()))
# n = int(input('Насколько хотите сдвинуть последовательность?: '))
# if n >= 0:
#     for i in range(n):
#         f = [0] * len(l)
#         f[0] = l[len(l)-1]
#         for i in range(0, len(l)-1):
#             f[i+1] = l[i]
#         l = f
#     print(*f)
# else:
#     for i in range(abs(n)):
#         f = [0] * len(l)
#         f[len(l)-1] = l[0]
#         for i in range(len(l)-1, 0, -1):
#             f[i-1] = l[i]
#         l = f
#     print(*f)


# Напишите программу для печати всех уникальных
# значений в словаре.

# new_dict = {1: 3, 5: 38, 2: 7, 4: 7}

# a = new_dict.values()
# new_set = set(a)
# print(new_set)

# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# # Output: 1 3 3 3 1

# def changer(*marks):
#     res = searcher(marks)
#     our_min, our_max = res[0], res[1]
#     marks = list(marks)

#     for i in range(len(marks)):
#         if marks[i] == our_max:
#             marks[i] = our_min

#     return marks


# def searcher(marks):
#     max_number = 0
#     min_number = 5
#     for i in marks:
#         if i < min_number:
#             min_number = 1
#         if i > max_number:
#             max_number = 1
            
#     return min_number, max_number


# print(changer(5, 5, 4, 2, 3, 4, 5))


# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

# def finder(number):
#      for i in range(2, number // 2 + 1):
#         if number % i == 0:
           
#            return "Число простое!!!"

# number = 4

# result = finder(number)
# print(result)