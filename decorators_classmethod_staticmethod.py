class MyClass():
    def foo(self, x):
        print "foo({0},{1})".format(self, x)

    @classmethod
    def class_foo(cls, x):
        print "class_foo({0},{1})".format(cls, x)

    @staticmethod
    def static_foo(x):
        print "static_foo({0})".format(x)

my = MyClass()
my.foo(1)
my.class_foo(1)
MyClass.class_foo(1)
my.static_foo(1)
MyClass.static_foo(1)
