class Star:
    def __init__(self, count: int):
        self.count = count

    # >
    def __gt__(self, other):
        return self.count > other.count

    def __add__(self, other):
        return Star(min(self.count + other.count, 5))


star_1 = Star(3)
star_2 = Star(5)
print(star_2 > star_1)
print(star_2 < star_1)
print((star_2 + star_1).count)