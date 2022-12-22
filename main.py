import log
from entities import create_new_student, create_new_grade


def my_start():

    while True:
        print('вы кто?')
        print('1.Студент\n2.Учитель\n3.Выход\n')
        num1 = input('ввод: ')

        if num1 == '1':
            print()
            print('1. посмотреть оценки')
            num2 = input('ввод: ')
            if num2 == '1':
                print('Для просмотра своих оценок вы должны ввести свой номер')
                answer = input('Вы его знаете? [y/n]').lower()
                if answer == 'n':
                    log.search_student()
                log.get_journal()

        elif num1 == '2':
            print('выберете')
            print('1. посмотреть список учеников')
            print('2. добавить ученика')
            print('3. добавить оценку')
            print('4. поиск ученика')
            num3 = input('ввод:')
            if num3 == '1':
                log.print_students(log.students_list())
            elif num3 == '2':
                log.append_student(create_new_student())
            if num3 == '3':
                print('Необходимо найти ученика:')
                log.search_student()
                log.append_grade(create_new_grade())
            if num3 == '4':
                log.search_student()
            else:
                input('неверный ввод.повторите: ')

        elif num1 == '3':
            print('До свидания!')
            break

        else:
            print('неверный ввод.повторите: ')


my_start()
