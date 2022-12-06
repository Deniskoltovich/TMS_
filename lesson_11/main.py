########## итераторы генераторы#######################33
numbers = [1, 2, 3]

for num in numbers:
    ...

iter_obj = iter(numbers)
while True:
    try:
        print(next(iter_obj))
    except StopIteration:
        break


class It:
    def __iter__(self):
        self.pos = 0
        self.items = [1, 2, 3]
        return self

    def __next__(self):
        if self.pos < len(self.items):
            self.current = self.pos
            self.pos += 1
            return self.items[self.current]
        else:
            raise StopIteration



#====================== generator =========================

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

gen = infinite_sequence()
for i in gen:
    print(i)