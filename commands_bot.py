from TurtleAPI import API


class Schedule:
    def __init__(self):
        self.api = API()
        self.group_list = self.api.take_group_list()['group']
        self.teacher_list = self.api.take_group_list()['teacher']
        self.schedule_for_groups = None
        self.group = None

    def check_group(self, group):
        if group in self.group_list:
            return True
        else:
            return False

    def get_schedule(self, group):
        self.schedule_for_groups = self.api.take_schedule_group(group)
        schedule_day = ''
        for i in self.schedule_for_groups['days']:
            schedule_day += i['day'] + '\n'
            for j in i['apairs']:
                for j1 in j['apair']:
                    schedule_day += f"\n{j['time']}\nПредмет -- {j1['doctrine']}\nПреподаватель: {j1['teacher']}\
                    \nАудитория: {j1['auditoria']}\nКорпус: {j1['corpus']}\n"

        return schedule_day

    @staticmethod
    def get_help():
        with open(file='text_info/text_help.txt', encoding='utf-8', mode='r') as file:
            text = ''
            for i in file:
                text += str(i)
        file.close()
        return text

    @staticmethod
    def get_calls():
        with open(file='text_info/calls.txt', encoding='utf-8', mode='r') as file:
            text = ''
            for i in file:
                text += str(i)
        file.close()
        return text
