import view
import init


def start_piont():
    path = 'school.json'
    school_data = init.init(path)
    school_group = list(school_data.keys())
    while True:
        menu = view.main_menu()
        if menu == '1':
            group = view.submenu('Выберите класс', school_group)
            view.show_group(school_data[group])
        elif menu == '2':
            view.show_all(school_data)
        elif menu == '3':
            exit()