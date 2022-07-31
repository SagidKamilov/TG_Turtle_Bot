import requests
import json
import datetime
import aiohttp


class API:
    def __init__(self):
        self.adr = 'http://45.155.207.232:8080/api/v2/'
        self.session = requests.session()

    def take_group_list(self):
        return self.session.get(self.adr + 'schedule/list').json()

    def take_schedule_group(self, group):
        return self.session.get(self.adr + 'schedule/{0}'.format(group)).json()

# Тесты и проверки
def ope():
    spis = {'days': [{'day': '21 июня, вторник', 'apairs': [{'time': '08:00  —  09:30', 'apair': [{'doctrine': 'Информатика', 'teacher': 'Федосеева  В.Ф.', 'auditoria': '401', 'corpus': '1', 'number': 1, 'start': '08:00', 'end': '09:30', 'warn': 'None'}]}, {'time': '09:40  —  11:10', 'apair': [{'doctrine': 'Литература', 'teacher': 'Лобова А.В.', 'auditoria': '318', 'corpus': '1', 'number': 2, 'start': '09:40', 'end': '11:10', 'warn': 'None'}]}, {'time': '11:30  —  13:00', 'apair': [{'doctrine': 'Человек в современном мире', 'teacher': 'Грицай О.П.', 'auditoria': '404', 'corpus': '1', 'number': 3, 'start': '11:30', 'end': '13:00', 'warn': 'None'}]}]}, {'day': '22 июня, вторник', 'apairs': [{'time': '08:00  —  09:30', 'apair': [{'doctrine': 'Информатика', 'teacher': 'Федосеева  В.Ф.', 'auditoria': '401', 'corpus': '1', 'number': 1, 'start': '08:00', 'end': '09:30', 'warn': 'None'}]}, {'time': '09:40  —  11:10', 'apair': [{'doctrine': 'Литература', 'teacher': 'Лобова А.В.', 'auditoria': '318', 'corpus': '1', 'number': 2, 'start': '09:40', 'end': '11:10', 'warn': 'None'}]}, {'time': '11:30  —  13:00', 'apair': [{'doctrine': 'Человек в современном мире', 'teacher': 'Грицай О.П.', 'auditoria': '404', 'corpus': '1', 'number': 3, 'start': '11:30', 'end': '13:00', 'warn': 'None'}]}]}], 'name': 'ИС-13'}
    schedule_day = ''
    for i in spis['days']:
        print(f"{i['day']}\n")
        for j in i['apairs']:
            print(j['time'])
            for k in j['apair']:
                print(f"Предмет -- {k['doctrine']}\nПрепод -- {k['teacher']}\nАудитория -- {k['auditoria']}\n")
    # for i in spis['days']:
    #     schedule_day += i['day']
    #     for j in i['apairs']:
    #         for j1 in j['apair']:
    #             schedule_day += f"\n{j['time']}\nПредмет -- {j1['doctrine']}\nПреподаватель: {j1['teacher']}\
    #             \nАудитория: {j1['auditoria']}\nКорпус: {j1['corpus']}\n"
