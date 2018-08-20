class People(object):
    count = 0

    def __init__(self, name):
        self.id = self.__new_id()
        self.name = name

    def __new_id(self):
        id = People.count
        People.count = People.count + 1
        return id

    def run(self):
        print('%s(%d) is running' % (self.name, self.id))

    def sleep(self):
        print('%s(%d) is sleeping' % (self.name, self.id))
