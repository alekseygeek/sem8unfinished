import csv

from entities import (
    STUDENT_ENTITY,
    JOURNAL_ENTITY,
    student_entry,
    grade_entry,
)


STUDENT_FILE = 'students.csv'
JOURNAL_FILE = 'journal.csv'
DELIMITER = ';'
STUDENT_HEADERS = tuple(STUDENT_ENTITY.keys())
JOURNAL_HEADERS = tuple(JOURNAL_ENTITY.keys())


def get_last_id(filename):
    """Получить последний индекс записей"""
    with open(filename, encoding='utf-8') as fd:
        csvreader = csv.DictReader(fd, delimiter=DELIMITER)
        listing = list(csvreader)
        if listing:
            return max(int(entry['id']) for entry in listing)
        return 0

def append_row(filename: str, entity: dict, fieldnames: tuple):
    """Добавить новую запись"""
    index = get_last_id(filename) + 1
    entity['id'] = index
    with open(filename, 'a', encoding='utf-8', newline='') as fd:
        csvwriter = csv.DictWriter(fd, delimiter=DELIMITER, fieldnames=fieldnames)
        csvwriter.writerow(entity)
    return index

def append_student(entity):
    """Добавить студента"""
    append_row(STUDENT_FILE, entity, STUDENT_HEADERS)

def append_grade(entity):
    """Добавить оценку"""
    append_row(JOURNAL_FILE, entity, JOURNAL_HEADERS)

# ------------------------------ Список записей ------------------------------ #

def entire_list(filename: str) -> list:
    with open(filename, encoding='utf-8') as fd:
        csvreader = csv.DictReader(fd, delimiter=DELIMITER)
        entry_list = list(csvreader)
    return entry_list

def students_list():
    """Добавить студента"""
    return entire_list(STUDENT_FILE)

def grades_list():
    """Добавить оценку"""
    return entire_list(JOURNAL_FILE)

# ----------------------------- Фильтрация списка ---------------------------- #

def filter_by_id(index, obj_list):
    return [entry for entry in obj_list if index == int(entry['id'])]

def filter_by_surname(string, obj_list):
    return [entry for entry in obj_list if string in entry['surname']]

def filter_by_number(number, obj_list):
    return [entry for entry in obj_list if number == int(entry['st_id'])]

# --------------------- Конвертирование записей в строки --------------------- #

def convert_student(obj_list):
    return [student_entry(entry) for entry in obj_list]

def convert_grade(obj_list):
    return [grade_entry(entry) for entry in obj_list]

# ------------------------------ Печать записей ------------------------------ #

def print_students(students):
    for line in convert_student(students):
        print(line)

def print_grades(grades):
    for line in convert_grade(grades):
        print(line)

# ----------------------------------- Поиск ---------------------------------- #

def search_student():
    print('Поиск по номеру или по фамилии или ее части')
    search_choice = input('Введите номер или фамилию: ')
    if search_choice.isdigit():
        print_students(filter_by_id(int(search_choice), students_list()))
    else:
        print_students(filter_by_surname(search_choice, students_list()))

# ------------------------------- Вывод оценок ------------------------------- #

def get_journal():
    search_number = int(input('Введите свой номер: '))
    print_grades(filter_by_number(search_number, grades_list()))


if __name__ == '__main__':
    print('last id:', get_last_id(STUDENT_FILE))
    # student = {'name': 'Петр', 'surname': 'Петров'}
    # append_student(student)

    print('-'*30)
    obj_list = students_list()
    # print(obj_list)
    print_students(obj_list)
    # print_students(students_list())
    print('-'*30)
    obj_list2 = filter_by_id(2, obj_list)
    print_students(obj_list2)
    print('-'*30)
    obj_list3 = filter_by_surname('ов', obj_list)
    print_students(obj_list3)