# Class object/ OOP


class Test:
    a = 10
    data = "Arun"


obj = Test()
print("obj data value is", obj.data)


# only data value is change in obj1
obj1 = Test()
obj1.data = "suman"
print("obj data value is", obj1.data)

obj2 = Test()
print("obj data value is", obj2.data)


class Test:
    a = 10
    data = a + 100

    def add(self):
        return self.data

    def result(self):
        self.name = "arjun"
        return self.add() + 10


obj = Test()
print(obj.result())
print(obj.name)


class Room:
    length = 10
    breadth = 20

    def mul(self):
        return self.length * self.breadth


obj = Room()
print(obj.mul())


class Bank_account:
    acc_no = 101011
    balance = 1200

    def result(self):
        return {"acc_no": self.acc_no, "balance": self.balance}


obj = Bank_account()
print(obj.result())


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b


obj = Math(1, 2)
print(obj.add())
