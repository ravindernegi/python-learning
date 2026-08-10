import sys
from time import sleep

print(sys.getrecursionlimit())  # check this limt of recursive by default

a = 0


def greet():
    global a
    print("Hello")

    if a < 10:
        a = a + 1
        greet()


greet()

# with sleep

a = 0


def greet():
    global a
    print("Hello2")
    sleep(0.02)
    if a < 50:
        a = a + 1
        greet()


greet()
