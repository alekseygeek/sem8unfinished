"""
Работает с записями (сущностями)

STUDENT_ENTITY, JOURNAL_ENTITY - словари объектов-сущностей
STUDENT_RECORD, JOURNAL_RECORD - основа для вывода строки
create_new_student(), create_new_grade() - создает новый объект-словарь для записи
student_entry(), grade_entry() - создает строку вывода
    из переданного объекта-словаря записи
"""


STUDENT_ENTITY = {
    'id': 'Номер',
    'surname': 'фамилия',
    'name': 'имя',
}

JOURNAL_ENTITY = {
    'id': 'Номер',
    'st_id': 'студент №',
    'science': 'предмет',
    'grade': 'оценка',
}

STUDENT_RECORD = (
    '{id}: %(id)s, {surname}: %(surname)s, {name}: %(name)s'
).format(**STUDENT_ENTITY)

JOURNAL_RECORD = (
    '{id}: %(id)s, {st_id} %(st_id)s, '
    '{science}: %(science)s, {grade}: %(grade)s'
).format(**JOURNAL_ENTITY)


def create_new_student():
    """Ввод данных студента"""
    new_entry = {}
    for column, line in STUDENT_ENTITY.items():
        if column != 'id':
            data = input('Введите данные ({}): '.format(line.capitalize()))
            new_entry[column] = data
    return new_entry

def student_entry(entity: dict):
    """Форматирование вывода студента"""
    return STUDENT_RECORD % entity

def create_new_grade():
    new_entry = {}
    for column, line in JOURNAL_ENTITY.items():
        if column != 'id':
            data = input('Введите данные ({}): '.format(line.capitalize()))
            new_entry[column] = data
    return new_entry

def grade_entry(entity: dict):
    return JOURNAL_RECORD % entity


if __name__ == '__main__':
    print(STUDENT_RECORD)
    print(JOURNAL_RECORD)

    print('-'*30)
    new_student = create_new_student()
    new_student['id'] = 5
    print(new_student)
    print(student_entry(new_student))

    print('-'*30)
    new_journal = create_new_grade()
    new_journal['id'] = 7
    print(new_journal)
    print(grade_entry(new_journal))
