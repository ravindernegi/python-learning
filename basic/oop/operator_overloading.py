# Operator Overloading in Python
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __str__(self):
        return f"₹{self.amount}"


m1 = Money(100)
m2 = Money(200)

m3 = m1 + m2

print(m3)
