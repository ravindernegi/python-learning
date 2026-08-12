# inheritance_demo.py


# =========================================================
# 1. SINGLE INHERITANCE
# =========================================================
# One child inherits from one parent.
#
# Animal
#   ↓
# Dog


class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


print("----- SINGLE INHERITANCE -----")

dog = Dog()

dog.eat()  # inherited from Animal
dog.bark()  # Dog's own method


# =========================================================
# 2. MULTILEVEL INHERITANCE
# =========================================================
# Grandparent → Parent → Child
#
# Animal
#   ↓
# Dog
#   ↓
# Puppy


class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


class Puppy(Dog):
    def cry(self):
        print("Puppy is crying")


print("\n----- MULTILEVEL INHERITANCE -----")

puppy = Puppy()

puppy.eat()  # Animal
puppy.bark()  # Dog
puppy.cry()  # Puppy


# =========================================================
# 3. MULTIPLE INHERITANCE
# =========================================================
# One child inherits from multiple parents.
#
# Father ──┐
#          ├── Child
# Mother ──┘


class Father:
    def father_skill(self):
        print("Father: Driving")


class Mother:
    def mother_skill(self):
        print("Mother: Cooking")


class Child(Father, Mother):
    def child_skill(self):
        print("Child: Coding")


print("\n----- MULTIPLE INHERITANCE -----")

child = Child()

child.father_skill()  # Father
child.mother_skill()  # Mother
child.child_skill()  # Child


# MRO = Method Resolution Order. It is the order in which Python searches classes for a method or attribute when inheritance is involved.

# This becomes especially important with multiple inheritance.


class A:
    def hello(self):
        print("A")


class B(A):
    def hello(self):
        print("B")


class C(A):
    def hello(self):
        print("C")


class D(B, C):
    pass


obj = D()

obj.hello()

print(D.mro())


# Using __init__() and super() with Inheritance


class user:

    def __init__(self):
        pass

    def get_name(name):
        print(name)


class user_b(user):

    def __init__(self):
        pass

    def get_name(name):
        super.get_name()


user_obj = user()
user.get_name("Ravi")
