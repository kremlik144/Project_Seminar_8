import controller as cntr
import interface as intr


# авторизация преподавателя
def authorization():
    dict_teachers = {}
    login = intr.authorization_person('Преподаватель')

    with open(f'database_teachers.txt', 'r', encoding="utf-8") as page:
        for i in range(1, 7):
            value = page.readline().split('; ')
            dict_teachers[value[0]] = value[1:]

    teachers = lst_teachers(login, dict_teachers)
    mod = cntr.correctness_of_values(intr.interface_teachers(teachers[0]), ['1', '2'])
    work(mod, teachers[1], teachers[0])


# поиск логина в базе учителей
def lst_teachers(login, dict_): 
    while True:
        if login in dict_.keys(): 
            print(f'\n{dict_[login][0]}! Здравствуйте!\n')
            return dict_[login]
        else:
            print('Пользователь отсутствует. Убедитесь в правильности введеного вами логина')
            login = intr.authorization_person('Преподаватель')


# просмотр и добавление дз
def work(mod, subject_, name):
    dict_learning = {}
    
    with open(f'learning_subjects.txt', 'r', encoding="utf-8") as page:
        for i in range(1, 7):
            value = page.readline().split(': ')
            dict_learning[value[0]] = value[1:]
    home_work = ''.join(dict_learning[subject_[:-1]])

    if mod == 1: print(f'\nДомашнее задание по предмету "{subject_[:-1]}" - {home_work}')
    else: 
        new_home_work = input(f'Введите новое задание по предмету {subject_[:-1]}: ')
        dict_learning[subject_[:-1]] = new_home_work + '\n'
        with open(f'learning_subjects.txt', 'w', encoding="utf-8") as page:
            for key in dict_learning.keys():
                new_work = ''.join(dict_learning[key])
                page.write(f'{key}: {new_work}')
                
    cyclicality(name, subject_)


# работа режима пока того хочет пользователь
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
            mod = cntr.correctness_of_values(intr.interface_teachers(name), ['1', '2'])
            work(mod, subject_, name)
            break
    else: 
        print(f'\nДо свидания, {name}!\n')
        return None
