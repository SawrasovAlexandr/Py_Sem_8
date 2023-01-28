# выбираем класс
# предмет
# ученика
# ставим оценку
# {3а:{вася: {математика: 1 2 3, физика: 3,2,4}, федя: {математика: 1 2 3, физика: 3,2,4}},
# 4а:{вася: {математика: 1 2 3, физика: 3,2,4}, федя: {математика: 1 2 3, физика: 3,2,4}} }




def submenu(text: str, item: list) -> str:
    while (result := input(f'{text} {tuple(item)}: ')).upper() not in map(str.upper, item):
        print('Некорректный ввод!')
    return result

def main_menu() -> str:
    result = ''
    while result not in ('1', '2'):
        print('1. Выбрать предмет\n'
              '2. Редактировать список класса\n')
        result = input('Выберите действие: ')
    return result
        

    
# kl = ['1А', '2А', '3А', '1Б', '2Б', '3Б']
# submenu('Выберите класс', kl)


