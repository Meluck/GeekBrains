"""
3. Реализовать базовый класс Worker (работник).

    определить атрибуты: name, surname, position (должность), income (доход);
    последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
    создать класс Position (должность) на базе класса Worker;
    в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
    проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

"""


print('GeekBrains homework #6, task 3')


class Worker:
    def __init__(self, name: str, surname: str, position: str, income=None):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'salary': 0.0,
                        'bonus': 0.0}
        if income is not None:
            self._income['salary'] = income[0]
            self._income['bonus'] = income[1]


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return self.name

    def get_total_income(self):
        worker_income = self._income
        return worker_income['salary'] + worker_income['bonus']


if __name__ == '__main__':
    pos = Position('Nil', 'Armstrong', 'cosmonaut', (300.01, 100.0))
    print(f'name = {pos.name}\nincome = {pos.get_total_income()}')
