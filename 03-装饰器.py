def outer(x):
    def inner(y):
        return x + y

    return inner


outer_func = outer(1)
print(outer_func)  # <function outer.<locals>.inner at 0x106e5bb80>
print(outer_func(2))  # 3
print(outer_func(3))  # 4


def hello(func):
    print(func, func.__name__)  # <function test at 0x103d3dca0>

    def _(*args, **kwargs):
        return "hello " + func(*args, **kwargs)

    return _


@hello
def test_hello(word):
    return word


print(test_hello("world"))  # hello world
print(test_hello("python"))  # hello python


def say(word):
    def _(func):
        def __(*args, **kwargs):
            res = f"{word} {func(*args, **kwargs)}"
            return res

        return __

    return _


@say("你好")
def test_say1(word):
    return word


@say("你好呀")
def test_say2(word):
    return word


print(test_say1("world"))  # 你好 world
print(test_say2("PyPy"))  # 你好呀 PyPy


def eat(food=None):
    def wrapper(func):
        def inner(*args, **kwargs):
            res = func(*args, **kwargs)
            print(res, food)
            return res

        return inner

    if callable(food):
        return wrapper(food)
    else:
        return wrapper


@eat  # 等于 eat(test_eat1)
def test_eat1():
    return "什么也不吃"


@eat("苹果")  # 等于 eat()(test_eat1)
def test_eat2():
    return "吃苹果"


def test_eat3():
    return "什么也不吃"


def test_eat4():
    return "吃哈哈"


def one_dec(func):
    print("one  start")

    def __(*args, **kwargs):
        print("one in")
        return func(*args, **kwargs)

    return __


def two_dec(func):
    print("two  start")

    def __(*args, **kwargs):
        print("two in")
        return func(*args, **kwargs)

    return __


@two_dec
@one_dec
def multi_test1():
    pass


def multi_test2():
    pass


two_dec(one_dec(multi_test2))()
