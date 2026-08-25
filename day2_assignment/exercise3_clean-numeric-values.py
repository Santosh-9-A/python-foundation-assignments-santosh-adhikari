'''Given:

raw_values = [100, None, 250, "invalid", 300, None, 450]
Create a new list containing only valid integers.

First solve it using:

A loop
continue
isinstance()
Expected result:

[100, 250, 300, 450]
Then solve it again using a list comprehension.'''

raw_values = [100, None, 250, "invalid", 300, None, 450]

valid_values = []

for value in raw_values:
    if not isinstance(value, int):
        continue
    valid_values.append(value)

print(valid_values)