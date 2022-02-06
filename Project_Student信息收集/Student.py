from re import S


class Student(object):
    def __init__(self, name, id, tel):
        self.name = name
        self.id = id
        self.tel = tel

    def __str__(self):
        return f'{self.name},{self.id},{self.tel}'


if __name__ == '__main__':
    aa = Student('koishi', 12, 180)
    print(type(aa))
