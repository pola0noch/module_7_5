# Домашнее задание по теме "Файлы в операционной системе".

import os
import time

directory = "."

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)  # Получаем полный путь к файлу
        filetime = os.path.getmtime(filepath)  # Получаем время последнего изменения файла
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))  # Форматируем время изменения
        filesize = os.path.getsize(filepath)  # Получаем размер файла в байтах
        parent_dir = os.path.basename(root)  # Получаем имя родительской директории

        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
              f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

_file = [f for f in os.listdir() if os.path.isfile(f)]
_dirs = [d for d in os.listdir() if os.path.isdir(d)]
print(_file, _dirs)

