# статические методы @staticmethod, @classmethod
import dataclasses


class X:
    @staticmethod
    def hello():
        print('hello')

    def hello_2(self):
        print('hello_2')


# X.hello() # ok
# X.hello_2() # not ok
# x = X()
# x.hello() #  ok
# x.hello_2() # ok

class StaticTest:
    def __init__(self):
        self.x = 10
        self.y = 20

    def method(self):
        self.a = 4

    @staticmethod
    def print_format():
        print(f"I'm static method")


x = StaticTest()
print(x.__dict__)
x.method()
print(x.__dict__)
StaticTest.print_format()


class Student:
    def __init__(self, first_name:str, last_name:str):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_string(cls, name_str: str):
        first_name, last_name = name_str.split()
        return cls(first_name, last_name)


s = Student('John', 'Wick')
t = Student.from_string('John Wick')


############################################################
#property


class H:
    def __init__(self, age = 0):
        self.__age = 0

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age if 0 <= age <= 120 else 0


h = H(30)
print(h.__dict__)
h.set_age(150)
print(h.__dict__)
h.__age = 150 # создает __age в классе, а на самом деле наша приватная переменная _H__age
print(h.__dict__)


class C:
    def __init__(self):
        self._x = None

    def getx(self):
        print('calling getx')
        return self._x

    def setx(self, value):
        print('callind setx')
        self._x = value

    def delx(self):
        print('calling delx')
        del self._x

    x = property(getx, setx, delx)


c = C()
print(c.x)
c.x = 10
print(c.x)
del c.x


class D:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        print('calling getx')
        return self._x

    @x.setter
    def x(self, value):
        print('callind setx')
        self._x = value

    @x.deleter
    def x(self):
        print('calling delx')
        del self._x



d = D()
print(d.x)
d.x = 10
print(d.x)
del d.x


#############################################################
# метаклассы

class MetaTest(type):
    count=0
    def __new__(cls, clsname, bases, attr):
        cls.count += 1
        print(cls, clsname, bases, attr)
        new_attrs = {k if k.startswith('_') else k.upper():
                     v for k,v in attr.items()}
        return type.__new__(cls, clsname, bases, attr)
    def __init_subclass__(cls, **kwargs):
        cls.count +=1



class Test(metaclass=MetaTest):
    x: str = '10'
    y: int = 20
    def __init__(self):
        self.x = "s"

    pass

print(Test.__dict__)
mt= Test()
mt2 = Test()
mt3 = Test()
print(MetaTest.count)

#################################################33333
# dataclass


@dataclasses.dataclass
class User:
    name: str
    password: str

u = User('hello', 'pas')
print(u)
