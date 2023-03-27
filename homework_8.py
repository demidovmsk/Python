# 1. Напишите функцию read_last(lines, file), которая будет открывать определенный файл file
# и выводить на печать построчно последние строки в количестве lines (на всякий случай проверим,
# что задано положительное целое число).
# Протестируем функцию на файле «article.txt» со следующим содержимым:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела


# lines = int(input('Введите строки: '))
# file = input('Введите путь к файлу article.txt: ')
# read_last(use_lines=lines, enter_file=file)

# def read_last(enter_file: str = 'article.txt', use_lines: int = 0):
#     try:
#         with open(f'{enter_file}', 'r', encoding="utf-8") as use_file:
#             data_list = use_file.readlines()


#         if 0 <= use_lines <= len(data_list):
#             for i in range(1, use_lines + 1):
#                 print(data_list[-i], end="")
#         else:
#             print("Введите допустимые значения строк,между null и count строками файла")


#     except FileNotFoundError as traceback:
#         print(f"File not found. Traceback: {traceback}")




# 1. Документ «article.txt» содержит следующий текст:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела
# Требуется реализовать функцию longest_words(file), которая записывает в файл result.txt слово,
# имеющее максимальную длину (или список слов, если таковых несколько).

# def longest_words(file):
#     with open((, , ='utf-8'))  text:
#     words = text.read().split()
#     max_length = len(max(words, key=len))
#         = = [word for word in words if len(word) == max_length]
#         if len(sought_words) == 1:
#             return sought_words[0]
#         return sought_words


# print(longest_words('article.txt'))

    
 

