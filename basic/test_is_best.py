# List, Tuple, Dictionary : In Python, lists, tuples, and dictionaries can contain each other in almost any combination, and they can be nested multiple levels.
# tuple : A tuple is immutable, which means its values cannot be changed after it is created.
tuple_var = ("Ravi", 40, "Cloud Eng")
print("===" + str(type(tuple_var)) + "===")

# Count tuple:
# It takes a value, searches through the entire list of tuples, and returns the count of matching values.
print(tuple_var.count(40))

# Get tuple's index:
# It takes a value,  searches through the entire list of tuples, and retunr match value index
print(tuple_var.index("Ravi"))

# Access Tuple by Index
print(tuple_var[1])


# List in python:
list_var = ["ravi", 39, "software eng."]
print("===" + str(type(list_var)) + "===")
list_var.append("Cloud+AI Eng.")
print(list_var[0] + " is moved from " + list_var[2] + " => " + list_var[3])

# reverse List:
list_var.reverse()
print(list_var)

# copy method:
numbers = [1, 2, 3]

new_numbers = numbers.copy()  # Now numbers and new_numbers are two separate lists:

print(new_numbers)
# [1, 2, 3]


# Dictionary in python:
dic_var = {"name": "ravi", "age": 39, "role": "software eng."}

print("Dictionary ===" + str((type(dic_var))) + "===")

dic_var.items

# set in python:
set_var = set()
set_var.add("Ravi")
set_var.add(40)
set_var.add("Ravi")
set_var.update({"Negi", 89, 45854})

print("set ===" + str(type(set_var)) + "===")


# Examples
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # Union:        {1, 2, 3, 4, 5}
print(a & b)  # Intersection: {3}
print(a - b)  # Difference:   {1, 2}


# Note: So if you're coming from JavaScript:
# JS                         Python
# ------------------------------------------------
# new Map()              →   {}
# map.set(k, v)          →   d[k] = v
# map.get(k)             →   d.get(k)
# map.has(k)             →   k in d
# map.delete(k)          →   del d[k]

# new Set()              →   set()
# set.add(x)             →   s.add(x)
# set.has(x)             →   x in s
# set.delete(x)          →   s.remove(x) / s.discard(x)


# Easy way to remember
# List
numbers = [1, 2, 3]

# Tuple
numbers = (1, 2, 3)

# Set
numbers = {1, 2, 3}

# Dictionary
person = {"name": "Ravi", "age": 39}

# One important gotcha:
{}  # dict
set()  # empty set
{1, 2, 3}  # set


# | Operation    | List         | Tuple        | Set          | Dictionary       |
# | ------------ | ------------ | ------------ | ------------ | ---------------- |
# | Add one      | `.append(x)` | ❌            | `.add(x)`    | `d[key] = value` |
# | Add multiple | `.extend(x)` | ❌            | `.update(x)` | `.update(x)`     |
# | Remove       | `.remove(x)` | ❌            | `.remove(x)` | `.pop(key)`      |
# | Check exists | `x in list`  | `x in tuple` | `x in set`   | `key in dict`    |
# | Length       | `len(x)`     | `len(x)`     | `len(x)`     | `len(x)`         |
# | Index access | `x[0]`       | `x[0]`       | ❌            | `x[key]`         |

# Deeply nested Python data structures, mixing dictionaries, tuples, lists, and sets.
# Dictionary
#   ↓
# Tuple
#   ↓
# 3Dictionary
#   ↓
# List
#   ↓
# Set

# ============================================
# Complex Nested Python Data Structure
#
# dict → tuple → dict → list → set
# ============================================

data = {
    "user": (
        {
            "name": "Ravi",
            "skills": [{"Python", "JavaScript", "SQL"}, {"React", "Node.js"}],
        },
    )
}


# --------------------------------------------
# Level 1: Dictionary
# --------------------------------------------

for dict_key, dict_value in data.items():

    print("Dictionary:")
    print("Key:", dict_key)

    # ----------------------------------------
    # Level 2: Tuple
    # ----------------------------------------

    for tuple_item in dict_value:

        print("  Tuple:")
        print("  Value:", tuple_item)

        # ------------------------------------
        # Level 3: Dictionary
        # ------------------------------------

        for user_key, user_value in tuple_item.items():

            print("    Dictionary:")
            print("    Key:", user_key)

            # --------------------------------
            # Level 4: List
            # --------------------------------

            if isinstance(user_value, list):

                for list_item in user_value:

                    print("      List:")
                    print("      Value:", list_item)

                    # ------------------------
                    # Level 5: Set
                    # ------------------------

                    if isinstance(list_item, set):

                        for set_item in list_item:

                            print("        Set:")
                            print("        Value:", set_item)
