# Polymorphism and Duck Typing
class Laptop:
    def build(self):
        print("Laptop Builds")


class Tablet:
    def open_pdf(self):
        print("open pdf")


class Alians:
    def code(self, machine: Laptop):
        print("Alians buliding")
        machine.build()


laptop_obj = Laptop()
tablet_obj = Tablet()

code_obj = Alians()
code_obj.code(laptop_obj)

code_obj.code(tablet_obj)
