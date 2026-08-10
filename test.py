# tuple : A tuple is immutable, which means its values cannot be changed after it is created.

tuple_var = ("Ravi",40,"Cloud Eng")
print(type(tuple_var))

# Count tuple:
# It takes a value, searches through the entire list of tuples, and returns the count of matching values.
print(tuple_var.count(40))

# Get tuple's index:
# It takes a value,  searches through the entire list of tuples, and retunr match value index 
print(tuple_var.index("Ravi"))

# Access Tuple by Index
print(tuple_var[1])