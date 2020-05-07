from typing import Iterable, Iterator, Generator


class Normal:
    pass


class IsIterable:
    def __iter__(self):
        pass


class ForNoIter:
    def __init__(self):
        self.params = [1, 2, 3, 4]

    def __getitem__(self, item):
        return self.params[item]


def test_iterable():
    check_objects = [Normal(), IsIterable(), ForNoIter(), list(), dict(), set(), tuple()]
    for obj in check_objects:
        print(f"{obj, isinstance(obj, Iterable)}")

    for i in ForNoIter():
        print(i)


class TestIterator:
    def __init__(self):
        self.index = 0
        self.params = [1, 2, 3]
        self.size = len(self.params)

    def __iter__(self):
        return iter(self.params)

    def __next__(self):
        while self.index < self.size:
            res = self.params[self.index]
            self.index += 1
            return res
        else:
            raise StopIteration()


def test_iterator():
    t = TestIterator()
    for element in t:
        print(element)

    check_objects = [Normal(), TestIterator(), list(), dict(), set(), tuple()]
    for obj in check_objects:
        print(f"{obj, isinstance(obj, Iterator)}")


class TestGenerator:

    @classmethod
    def print_num_unit_le_0(cls, num):
        while num > 0:
            yield num
            num -= 1

    @classmethod
    def print_list_generator(cls, num):
        return (i for i in range(num))


def test_generator():
    check_objects = [TestGenerator.print_list_generator(3), TestGenerator.print_num_unit_le_0(3)]
    for obj in check_objects:
        print(f"{obj, isinstance(obj, Generator)}")
    for i in TestGenerator.print_num_unit_le_0(3):
        print(i)
    print("-------")
    for i in TestGenerator.print_list_generator(3):
        print(i)


if __name__ == '__main__':
    test_iterable()
    test_iterator()
    test_generator()
