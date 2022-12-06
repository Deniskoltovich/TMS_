class A:
    def talk(self): print('A')


class B(A):
    def __init__(self):
        super().__init__()

    def talk(self): print('B')


class C(B):
    # def talk(self): print("C")
    def __init__(self):
        B.__init__(self)


c = C()
c.talk()

super(B, c).talk()
# super - работаем с родиетельскими классами
# ищем после В
# c - объект с которым работаем
# class super(type, object_or_type=None)