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


print(Foo().bar)
foo1 = Foo1()
print(foo1.bar)
foo1.bar1 = '_1'
print(foo1.bar1)
print(Foo2()._bar)
# print(Foo2().__bar)   # can not access '__bar' via this way
print(Foo2()._Foo2__bar)
print(Foo3().bar)


print()
print('#'*10)
print()


class Clsvar(object):
    foo = '123'


print(Clsvar().foo)
clsvar1 = Clsvar()
clsvar2 = Clsvar()
print(clsvar1.foo)
print(clsvar2.foo)
clsvar1.foo = '321'
print(clsvar1.foo)
print(clsvar2.foo)
Clsvar.foo = 'abc'
print(clsvar1.foo)
print(clsvar2.foo)
