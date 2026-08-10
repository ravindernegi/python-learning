# ==========================================
# 1. LIST - Access using index
# ==========================================

my_list = ["apple", "banana", "mango"]

print("LIST")
print(my_list[0])  # apple
print(my_list[1])  # banana
print(my_list[2])  # mango


# ==========================================
# 2. TUPLE - Access using index
# ==========================================

my_tuple = ("apple", "banana", "mango")

print("\nTUPLE")
print(my_tuple[0])  # apple
print(my_tuple[1])  # banana
print(my_tuple[2])  # mango


# ==========================================
# 3. DICTIONARY - Access using key
# ==========================================

person = {"name": "John", "age": 25, "city": "Delhi"}

print("\nDICTIONARY")

# Access using key []
print(person["name"])  # John
print(person["age"])  # 25

# Access using get()
print(person.get("name"))  # John
print(person.get("age"))  # 25

# If key does not exist
print(person.get("country"))  # None

# get() with default value
print(person.get("country", "Not Found"))  # Not Found


# ==========================================
# 4. SET - No index and no key
# ==========================================

my_set = {"apple", "banana", "mango"}

print("\nSET")

# Check whether a value exists
print("apple" in my_set)  # True
print("orange" in my_set)  # False

# Loop through a set
for item in my_set:
    print(item)


my_list = ["apple", "banana"]
print(my_list[0])

my_tuple = ("apple", "banana")
print(my_tuple[0])

my_dict = {"name": "John"}
print(my_dict["name"])
print(my_dict.get("name"))

my_set = {"apple", "banana"}
print("apple" in my_set)


# The shortest rule:

# 🟢 List → collection that changes
# 🔵 Tuple → collection that doesn't change
# 🟡 Dictionary → key-value information
# 🔴 Set → unique values
