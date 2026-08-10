# Simple shallow copy: Now numbers and new_numbers are two separate lists:

numbers = [1, 2, 3]

new_numbers = numbers.copy()

print(new_numbers)
# [1, 2, 3]

new_numbers.append(4)

print(numbers)
# [1, 2, 3]

print(new_numbers)
# [1, 2, 3, 4]

# both variables refer to the same list:
# numbers ─────┐
#             ↓
#          [1, 2, 3]
#             ↑
# new_numbers ─┘

# The easiest way to understand shallow copy vs deep copy is with a nested list.

# 1. Shallow Copy : A shallow copy creates a new outer object, but the nested objects are still shared.

import copy

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)

shallow[0].append(5)

print(original)
# [[1, 2, 5], [3, 4]]

print(shallow)
# [[1, 2, 5], [3, 4]]


# 2. Deep Copy:  A deep copy creates a new outer object and new nested objects.

original = [[1, 2], [3, 4]]

deep = copy.deepcopy(original)

deep[0].append(5)

print(original)
# [[1, 2], [3, 4]]

print(deep)
# [[1, 2, 5], [3, 4]]
