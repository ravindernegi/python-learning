class demo_class:

    name = "Java"  # class vairable

    def __new__(cls):  # Construct
        print("Construct")
        return super().__new__(cls)

    def __init__(self):
        self.name = "Python"  # with self is like a this keyword of javascript
        print("init")

    def main(self, str):
        print("Hello Python", str)

    @classmethod
    def info(self):
        print(self.name)

    @staticmethod
    def test():
        print("static method")


obj = demo_class()
print(type(obj))

obj.main(" is best")
print(obj.name)


a = 4
print(type(a))


# __new__ → creates/allocates the object
# __init__ → initializes the already-created object
# self → current instance/object
# cls → current clas


print(obj.info())

print(type(obj.test()))
