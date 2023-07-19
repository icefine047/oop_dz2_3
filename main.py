#ЗАДАНИЕ 3

import os

current = os.getcwd()
folder = 'sorted'
file_name_1 = '1.txt'
file_name_2 = '2.txt'
file_name_3 = '3.txt'
file_name_4 = 'new.txt'

with open(file_name_1, 'r', encoding='utf-8') as file1 , open(file_name_2, 'r', encoding='utf-8') as file2 , open(file_name_3, 'r', encoding='utf-8') as file3 , open(file_name_4, 'w', encoding='utf-8') as new_file:
    dict_file = {
        file1 : [len(file1.readlines()), file_name_1],
        file2 : [len(file2.readlines()), file_name_2],
        file3 : [len(file3.readlines()), file_name_3]
    }

    dict_file_sort = dict(sorted(dict_file.items(), key=lambda item : item[1][0]))
    file1.seek(0)
    file2.seek(0)
    file3.seek(0)

    for keys, values in dict_file_sort.items():
        new_file.writelines(f'{values[1]}\n')
        new_file.writelines(f'{values[0]}\n')
        for line in keys.readlines():
            new_file.writelines(f'{line}')
        new_file.writelines('\n')