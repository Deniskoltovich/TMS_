# first approach
from functools import singledispatch
# это для перегрузки методов

class Human:

    # init это конструктор класса Human
    # self - объект текущего класса, можно на его месте писать что угодно
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age



    def talk(self):
        print(f'{self.name} is talking...')


class Student(Human):
    def __init__(self, name: str, age: int, ticket: str):
        super().__init__(name, age)
        self.ticket = ticket


    def study(self, lesson: str):
        print(f'{self.name} is studying {lesson}')


denis = Human('Denis', 18)
john = Student('John', 56, '1234')
# denis.name = 'Denis Koltovich' # все поля в питоне публичные
# denis.age = 18
# john.name = 'John Wick' # все поля в питоне публичные
# john.age = 56

print(denis.__dict__, denis.talk(), sep='\n')
print(john.study('math'))







