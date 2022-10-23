import controller as cntr
import interface as intr


# авторизация студента
def authorization():
    dict_student = {}
    login = intr.authorization_person('Ученик')

    with open(f'database_students.txt', 'r', encoding="utf-8") as page:
        for i in range(1, 7):
            value = page.readline().split('; ')
            dict_student[value[0]] = value[1:]

    student = lst_student(login, dict_student)
    
    mod = cntr.correctness_of_values(intr.interface_student(student), [str(i) for i in range(1, 7)])
    view_work(mod, student)


# поиск логина в базе студентов
def lst_student(login, dict_):
    
    while True:
        if login in dict_.keys():
            name = ''.join(dict_[login])
            print(f'\n{name[:-1]}! Здравствуйте!\n')
            return name[:-1]
        else:
            print('Пользователь отсутствует. Убедитесь в правильности введеного вами логина')
            login = intr.authorization_person('Ученик')


# просмотр  дз
def view_work(mod, name):
    dict_learning = {}
    
    with open(f'learning_subjects.txt', 'r', encoding="utf-8") as page:
        for i in range(1, 7):
            value = page.readline().split(': ')
            dict_learning[i] = value

    print(f'\n{name}, ДЗ по предмету {dict_learning[mod][0]} - {dict_learning[int(mod)][1][:-1]}\n')
    cyclicality(name, mod)


# цикличность действий
def cyclicality(name, subject_):
    flag = ''
    while True:
        otwet = input('Хотите продолжить? Введите Yes или No: ')
        if otwet in ['Yes', 'No']: 
            flag = otwet
            break
        else: intr.orrectness_of_values_intr()

    if flag == 'Yes':
        while otwet:
            mod = cntr.correctness_of_values(intr.interface_student(name), [str(i) for i in range(1, 7)])
            view_work(mod, name)
            break
    else: 
        print(f'\nДо свидания, {name}!\n')
        return None