from collections import Iterable


class Classmate(object):
    def __init__(self):
        self.names = list()
        self.current = 0

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        """如果想要一个对象成为一个可迭代的对象，必须实现__iter__方法"""
        return self

    def __next__(self):

        if self.current < len(self.names):
            ret = self.names[self.current]
            self.current += 1
            return ret
        else:
            raise StopIteration



classmater = Classmate()
classmater.add('老王')
classmater.add('老张')
classmater.add('老陶')

print('判断是否是可迭代对象:', isinstance(classmater, Iterable))
for i in classmater:
    print(i)
