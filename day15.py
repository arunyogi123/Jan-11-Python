# Inheritance
# Single
# Multiple
# Multilevel


# class Parent():

#     def __init__ (self):
#         print("I am here")

#     a=100
#     data=1

# class Child(Parent):

#     data=100

#     def __init__(self,a1,b1):
#         self.a1=a1
#         print("i am not here")
#         Parent. __init__(self)

#     def test(self):
#         return f"i am from Child method and value of a is{self.a}"

# obj=Child(1,2)
# print(obj.test())


# class Employee():
#     name='Arun'
#     emp_id=10101
#     basic_salary=100000

# class Manager(Employee):
#     bonus=10

#     def annual_salary(self):
#         amount=self.basic_salary*12
#         bonus_amt=amount*(self.bonus/100)
#         return amount+self.bonus

# obj=Manager()
# print(obj.annual_salary())


class Account:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance

    def display_acc_details(self):
        return f"The acc_no is {self.acc_no} and its balance is {self.balance}"


class Saving_acc(Account):

    def __init__(self, acc_no, balance, int_rate):
        super().__init__(acc_no, balance)
        self.int_rate = int_rate

    def int_amt(self):
        interest = (self.balance * self.int_rate) / 100
        return f"and its interest rate is {interest}"


obj = Saving_acc(101010, 10000, 10)
print(obj.display_acc_details())
print(obj.int_amt())
