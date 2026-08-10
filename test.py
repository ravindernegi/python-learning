# tuple : A tuple is immutable, which means its values cannot be changed after it is created.
tuple_var = ("Ravi",40,"Cloud Eng")
print('===' + str(type(tuple_var)) + '===')

# Count tuple:
# It takes a value, searches through the entire list of tuples, and returns the count of matching values.
print(tuple_var.count(40))

# Get tuple's index:
# It takes a value,  searches through the entire list of tuples, and retunr match value index 
print(tuple_var.index("Ravi"))

# Access Tuple by Index
print(tuple_var[1])


# List in python:
list_var = ["ravi",39,"software eng."]
print('===' + str(type(list_var)) + '===')
list_var.append('Cloud+AI Eng.')
print(list_var[0] +' is moved from '+ list_var[2] + ' => '+ list_var[3])

# reverse List:
list_var.reverse()
print(list_var)

#copy method: 
numbers = [1, 2, 3]

new_numbers = numbers.copy() # Now numbers and new_numbers are two separate lists:

print(new_numbers)
# [1, 2, 3]




