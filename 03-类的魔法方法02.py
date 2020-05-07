"""
    描述器: Python 有三个特殊方法，__get__、__set__、__delete__，用于覆盖属性的一些默认行为，如果一个类定义了其中一个方法，那么它的实例就是描述器
        访问: __get__(self, instance, cls) # instance 代表实例本身，cls 表示类本身，使用类直接访问时，instance 为 None
        赋值: __set__(self, instance, value) # instance 为实例，value 为值
        删除: __delete__(self, instance) # instance 为实例
"""


class MyDescriptor:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val

    def __get__(self, instance, owner):
        print(instance, owner)
        print("Get", self.key)
        return self.val

    def __set__(self, instance, value):
        print(instance)
        print("Set", self.key)
        self.val = value

    def __delete__(self, instance):
        print(instance)

    def __getattribute__(self, item):
        res = object.__getattribute__(self, item)
        if hasattr(res, "__get__"):
            return res.__get__(None, self)
        return res


class Test:
    md1 = MyDescriptor("zz", 20)
    md2 = MyDescriptor("ff", 30)


if __name__ == '__main__':
    test = Test()
    print(test.md1)
    test.md1 = 120
