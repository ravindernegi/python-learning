def display(num):
    return num

def perform(num, call_back): 
    result = call_back(num)
    print (result)


count = 10
perform(count, display)



# Note: perform is the Higher order function 