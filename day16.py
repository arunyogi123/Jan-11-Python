# class Order():
#     order_id=1111
#     order_amt=1000

#     def order_amt(self):
#         return f' order_id = {self.order_id} and order_amt = {self.order_amt}'

# class Online_order(Order):
#     delivery_charge=200

#     def online_order_amt(self):
#         return f'delivery charge = {self.delivery_charge}'

#     def total_amt(self):
#         total_amount=self.order_amt+self.delivery_charge
#         return total_amount

# class International_order(Online_order):
#     order_limit=50
#     custom_duty=90


class Order:
    order_id = 1
    order_amount = 100

    def calculate_total(self):
        print("Order: Base amount")
        return self.order_amount


class OnlineOrder(Order):
    delivery_charge = 10

    def calculate_total(self):
        total = super().calculate_total()
        print("OnlineOrder: Adding delivery charge")
        return total + self.delivery_charge


class InternationalOrder(OnlineOrder):
    duty_limit = 10000
    custom_duty = 1200

    def calculate_total(self):
        total = super().calculate_total()
        if self.order_amount > self.duty_limit:
            print("InternationalOrder: Adding customs duty")
            total += self.customs_duty
        else:
            print("InternationalOrder: No customs duty applied")
        return total


order = InternationalOrder()

print("\nFinal Payable Amount:", order.calculate_total())


class Order:
    def __init__(self, order_id, order_amt):
        self.order_id = order_id
        self.order_amt = order_amt

    def calculate_total(self):
        print("Order: Base amount")
        return self.order_amt


class OnlineOrder(Order):
    def __init__(self, order_id, order_amt, delivery_charge):
        super().__init__(order_id, order_amt)
        self.delivery_charge = delivery_charge

    def calculate_total(self):
        total = super().calculate_total()
        print("OnlineOrder: Adding delivery charge")
        return total + self.delivery_charge


class InternationalOrder(OnlineOrder):
    def __init__(self, order_id, order_amt, delivery_charge, duty_limit, custom_limit):
        self.duty_limit = duty_limit
        self.custom_limit = custom_limit
        super().__init__(order_id, order_amt, delivery_charge)

    def calculate_total(self):
        total = super().calculate_total()
        if self.order_amt > self.duty_limit:
            print("InternationalOrder: Adding customs duty")
            total += self.custom_limit
        else:
            print("InternationalOrder: No customs duty applied")
        return total


order = InternationalOrder(101, 10000, 10, 50, 90)

print("\nFinal Payable Amount:", order.calculate_total())
