from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UpiPayment(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class CardPayment(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


# UPI payment
upi = UpiPayment()
upi.pay(1000)

# Card payment
card = CardPayment()
card.pay(2000)
