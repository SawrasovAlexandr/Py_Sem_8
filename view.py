

def submenu(text: str, item: list) -> str:
    while (result := input(f'{text} {tuple(item)}: ')).upper() not in map(str.upper, item):
        print('Некорректный ввод!')
    return result

def main_menu() -> str:
    result = ''
    while result not in ('1', '2', '3'):
        print('1. Выбрать класс\n'
              '2. Показать всех\n'
              '3. Выход\n')
        result = input('Выберите действие: ')
        print()
    return result
        
def show_group(group_dict) -> None:
    title = 'Ученики / Предметы'
    temp = list(group_dict.keys())
    title_obj = list(group_dict[temp[0]].keys())
    print(f'{title:20}', end='')
    for item in title_obj:
        print(f' | {item:>12}', end='')
    print('\n', '-' * 65)
    for item in temp:
        print(f'{item:20}', end='')
        for i in title_obj:
            rep = list(map(str, group_dict[item].get(i)))
            report = ' '.join(rep)
            print(f' | {report:>12}', end='')
        print()
    print()

def show_all(all_dict):
    groups = list(all_dict.keys())
    for group in groups:
        print(group)
        show_group(all_dict[group])
