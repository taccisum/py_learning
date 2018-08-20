# -*- coding:utf8 -*-


class Foo(object):
    bar = '0'


class Foo1(object):

    def __init__(self):
        self.bar = '1'


class Foo2(object):

    def __init__(self):
        self._bar = '2'
        self.__bar = '_2'


print(Foo().bar)
foo1 = Foo1()
print(foo1.bar)
foo1.bar1 = '_1'
print(foo1.bar1)
print(Foo2()._bar)
# print(Foo2().__bar)   # can not access '__bar' via this way
print(Foo2()._Foo2__bar)
