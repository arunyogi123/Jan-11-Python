class A:
    __private_attrs = 100
    public_attrs = __private_attrs


class B(A):
    __private_attrs = 1000

    def test(self):
        print(self.__private_attrs)
        return "this is for private attrs"


obj = B()
print(obj.test())


class A:
    __private_attrs = 100
    public_attrs = __private_attrs


class B(A):
    __private_attrs = 100

    def __test(self):
        print(self.__private_attrs)
        return "this is for private attrs"

    def hello(self):
        return self.__test()


obj = B()
print(obj.hello())


class Amount:

    __balance = 1000
    public_balance = __balance - 100


class Deposit(Amount):

    def update(self, amt):
        self.__amt = self.__amt + amt


obj = Deposit()
