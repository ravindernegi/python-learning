# Polymorphism and Duck Typing
class laptop:
    def build(self):
        print("Laptop Builds")


class tablet:
    def open_pdf(self):
        print("open pdf")


class alians:
    def code(self, machine: laptop):
        print("Alians buliding")
        machine.build()


laptop_obj = laptop()
tablet_obj = tablet()

code_obj = alians()
code_obj.code(laptop_obj)

code_obj.code(tablet_obj)
