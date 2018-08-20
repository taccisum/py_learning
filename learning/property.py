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


class Foo3(Foo1):
    pass


assert Foo().bar is '0'
foo1 = Foo1()
assert foo1.bar is '1'
foo1.bar1 = '_1'
assert foo1.bar1 is '_1'
assert Foo2()._bar is '2'
# print(Foo2().__bar)   # can not access '__bar' via this way
assert Foo2()._Foo2__bar is '_2'
assert Foo3().bar is '1'


class Clsvar(object):
    foo = '123'


assert Clsvar().foo is '123'
clsvar1 = Clsvar()
clsvar2 = Clsvar()
assert clsvar1.foo is '123'
assert clsvar2.foo is '123'
clsvar1.foo = '321'
assert clsvar1.foo is '321'
assert clsvar2.foo is '123'
Clsvar.foo = 'abc'
assert clsvar1.foo is '321'
assert clsvar2.foo is 'abc'
