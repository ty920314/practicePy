from collections import Iterable


class ClassIterator(object):
    def __init__(self, obj):
        self.obj = obj
        self.current = 0

    def __iter__(self):
        pass

    def __next__(self):
        self.current += 1
        if self.current < self.current:
            ret = self.obj.names[0]
            return ret
        else:
            raise StopIteration


class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        """如果想要一个对象成为一个可迭代的对象，必须实现__iter__方法"""
        return ClassIterator(self)


classmater = Classmate()
classmater.add('老王')
classmater.add('老张')
classmater.add('老陶')

print('判断是否是可迭代对象:', isinstance(classmater, Iterable))
for i in classmater:
    print(i)
