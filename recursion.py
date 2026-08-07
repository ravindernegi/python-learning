import sys

print(sys.getrecursionlimit()) # check this limt of recursive by default

a = 0

def greet():
    global a
    print("Hello")
    
    if a < 10:
        a = a + 1
        greet()

greet()