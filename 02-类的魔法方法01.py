class Test:
    class_prop = 1

    def __init__(self):
        self.prop = 2

    def __getitem__(self, item):
        """帮助实例可以通过[]运算符获取内容"""
        print(f"{item} go __getitem__")
        return item

    def __getattr__(self, item):
        """
            当访问一个实例的属性时，如果这个属性不存在会走到这里来，但是当 __getattr__ 和 __getattribute__同时存在的时，会走__getattribute__。
        """
        return "default"

    def __getattribute__(self, item):
        """
            属性访问拦截器
                1、只要调用实例的任何属性都会走一次这个方法，
                2、如果重写这个方法需要谨慎处理，稍有不当就会造成死循环。比如在这个方法里调用 实例方法或者属性。
        """
        print(f"{item} go __getattribute__ ")
        return super(Test, self).__getattribute__(item)


if __name__ == "__main__":
    test = Test()
    print(test[3])
    print("\n------------\n")
    print(test.a2)
