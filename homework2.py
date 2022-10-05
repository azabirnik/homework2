# Aleksei Zabirnik <azabirnik@gmail.com>
# Avito Academy homework 2


def get_choice() -> int:
    """ Give user a choice: 1, 2 or 3 """
    print('Меню:\n\
1. Вывести в понятном виде иерархию команд, т.е. департаменти \
все команды, которые входят в него\n\
2. Вывести сводный отчёт по департаментам: название, численность, "вилка" \
зарплат в виде мин – макс, среднюю зарплату\n\
3. Сохранить сводный отчёт из предыдущего пункта в output.csv. При \
этом необязательно вызывать сначала команду из п.2')
    choice = 0
    while choice not in range(1, 4):
        print('Введите 1, 2 или 3 и нажмите Enter: ', end='')
        try:
            choice = int(input())
        except ValueError as ve:
            pass
    print()
    return choice


def load_data(file_name: str) -> dict:
    """ Load data from CSV file (utf-8 encoding) and return a dict of departments """
    departments = {}
    with open(file_name, 'r+t', encoding='utf-8') as data_file:
        for line in data_file.readlines()[1:]:
            new_person = line[:-1].split(';')
            department = new_person.pop(1)
            new_person[3] = float(new_person[3])
            new_person[4] = float(new_person[4])
            if department not in departments.keys():
                departments[department] = []
            departments[department].append(new_person)
    return departments


def choice1_hierarchy(departments: dict) -> None:
    """ Print the hierarchy of teams """
    for department, employees in departments.items():
        units = []
        for employee in employees:
            if employee[1] not in units:
                units.append(employee[1])
        print(f'Департамент: {department}. Отделы: {", ".join(units)}')


def choice2_print_summary(departments: dict) -> None:
    """ Print the summary for departments: how many employees, min, max and avg salary """
    for department, employees in departments.items():
        salaries = []
        for employee in employees:
            salaries.append(employee[4])
        print(f'Департамент: {department}. Количество сотрудников: {len(salaries)}, \
минимальная зарплата: {min(salaries)}, максимальная зарплата: {max(salaries)}, \
средняя зарплата: {round(sum(salaries)/len(salaries), 2)}.')


def choice3_save_summary(departments: dict) -> None:
    """ Save the summary for departments in output.csv: how many employees, min, max and avg salary """
    file_name = 'output.csv'
    output_str = 'Департамент;Количество сотрудников;Минимальная зарплата;\
Максимальная зарплата;Средняя зарплата\n'
    for department, employees in departments.items():
        salaries = []
        for employee in employees:
            salaries.append(employee[4])
        output_str += f'{department};{len(salaries)};{min(salaries)};{max(salaries)};\
{round(sum(salaries)/len(salaries), 2)}\n'
    with open(file_name, 'w+t', encoding='utf-8') as output_file:
        output_file.write(output_str)


if __name__ == '__main__':
    departments = load_data('Corp_Summary.csv')
    options = {1: choice1_hierarchy, 2: choice2_print_summary, 3: choice3_save_summary}
    options[get_choice()](departments)
