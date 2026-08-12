class DemoClass:

    name = "Java"

    def __init__(self):
        self.name = "Python"  # with self is like a this keyword of javascript
        print("init")

    def main(self, str):
        print("Hello Python", str)


obj = DemoClass()
print(type(obj))

obj.main(" is best")
print(obj.name)


a = 4
print(type(a))
