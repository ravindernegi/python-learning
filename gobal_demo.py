a = 10
print(10)

def do():
    print(globals()['a']) # Global variable get by globals function
    print("inside :", a)


do()

print("outside :",a)