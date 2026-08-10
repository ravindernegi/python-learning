def outer():
    print("Outer fun")

    def inner():
        print("Inner fun")

    return inner


do_action = outer()
do_action()