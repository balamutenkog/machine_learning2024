import csv
import json
from datetime import datetime, timedelta

employees = [
    {"ФИО": "Иванов Иван Иванович", "Должность": "Менеджер", "Дата найма": "22.10.2013", "Оклад": 250000},
    {"ФИО": "Сорокина Екатерина Матвеевна", "Должность": "Аналитик", "Дата найма": "12.03.2020", "Оклад": 75000},
    {"ФИО": "Струков Иван Сергеевич", "Должность": "Старший программист", "Дата найма": "23.04.2012", "Оклад": 150000},
    {"ФИО": "Корнеева Анна Игоревна", "Должность": "Ведущий программист", "Дата найма": "22.02.2015", "Оклад": 120000},
    {"ФИО": "Старчиков Сергей Анатольевич", "Должность": "Младший программист", "Дата найма": "12.11.2021", "Оклад": 50000},
    {"ФИО": "Бутенко Артем Андреевич", "Должность": "Архитектор", "Дата найма": "12.02.2010", "Оклад": 200000},
    {"ФИО": "Савченко Алина Сергеевна", "Должность": "Старший аналитик", "Дата найма": "13.04.2016", "Оклад": 100000},
]

def calculate_bonus(employees):
    for employee in employees:
        if "программист" in employee["Должность"].lower():
            employee["Премия"] = employee["Оклад"] * 0.03
        else:
            employee["Премия"] = 0

def calculate_holiday_bonus(employees):
    for employee in employees:
        if employee["ФИО"].endswith('на'):
            employee["Премия_по_празднику"] = 2000  # 8 марта
        else:
            employee["Премия_по_празднику"] = 2000  # 23 февраля

def salary_indexation(employees):
    for employee in employees:
        hire_date = datetime.strptime(employee["Дата найма"], "%d.%m.%Y")
        years_worked = (datetime.now() - hire_date).days / 365
        if years_worked > 10:
            employee["Индексация"] = employee["Оклад"] * 0.07
        else:
            employee["Индексация"] = employee["Оклад"] * 0.05

def create_leave_list(employees):
    leave_list = []
    for employee in employees:
        hire_date = datetime.strptime(employee["Дата найма"], "%d.%m.%Y")
        if (datetime.now() - hire_date) >= timedelta(days=183):  # 6 месяцев
            leave_list.append(employee["ФИО"])
    return leave_list

def write_to_csv(employees, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=employees[0].keys())
        writer.writeheader()
        writer.writerows(employees)

def write_to_json(employees, filename):
    with open(filename, mode='w', encoding='utf-8') as jsonfile:
        json.dump(employees, jsonfile, ensure_ascii=False, indent=4)

calculate_bonus(employees)
calculate_holiday_bonus(employees)
salary_indexation(employees)
leave_list = create_leave_list(employees)

write_to_csv(employees, 'employees.csv')
write_to_json(employees, 'employees.json')

print("Список сотрудников, отработавших более 6 месяцев:")
print(leave_list)