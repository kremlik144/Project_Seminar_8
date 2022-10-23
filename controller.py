import interface as intr
import teachers as ths
import student as stn


# выбор режима работы
def mod_work():
    value = intr.hello_mod()
    mod = correctness_of_values(value, ['1', '2'])
    if mod == 1: ths.authorization()
    else: stn.authorization()


# проверка корректности ввода режима работы
def correctness_of_values(value, lst):
    while True:
        if value in lst: return int(value)
        else: value = intr.orrectness_of_values_intr()