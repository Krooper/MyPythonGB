# 3 - В файле, содержащем фамилии студентов и их оценки,
# изменить на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Андрей Валетов 5
# Фредди Меркури 3
# Анастасия Пономарева 4
#
# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# АНДРЕЙ ВАЛЕТОВ 5
# Фредди Меркури 3
# Анастасия Пономарева 4

# Функция, которая создает словарь их учеников и их оценок
def file_reader(file):
    students_dict = {}
    with open(file, 'r', encoding='utf-8') as students:
        for line in students:
            line = line.split(' ')
            line[-1] = line[-1].replace('\n', '')
            student = " ".join(line[0:2])
            mark = line[2]
            students_dict[student] = mark
    return students_dict


# Функция, создающая новый словарь, отредактированный в зависимости от оценки
def new_students_dict(dictionary):
    edited_students_dict = {}
    for key, value in dictionary.items():
        if int(value) > 4:
            student = key.upper()
            edited_students_dict[student] = value
        else:
            edited_students_dict[key] = value
    return edited_students_dict


    # Записываем словарь в файл
def file_writer(file, dictionary):
    with open(file, 'w', encoding='utf-8') as students:
        for key, value in dictionary.items():
            students.write(f'{key} {value}\n')

# Перезаписываем файл
file_writer('students.txt', new_students_dict(file_reader('students.txt')))

# Выводим аналогичный результат в консоль
print(new_students_dict(file_reader('students.txt')))
