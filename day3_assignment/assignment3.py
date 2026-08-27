'''What a function analyze_numbers(numbers) that takes a list of numbers and retuens four values in this order:

the smallest number.
the largest number.
the sum of all numbrts.
the numbers sorted in descending order(as a list).

Use the built-in functions min(), max(), sum(), and sorted() - do not calculate these manually with loops.

simple call and expected output:

samllest, largest, total, desc = analyze_numbers([4, 9, 1, 7, 3])
print(smallest)
print(largest)
print(total)
print(decs)

'''

# Write your code here

def analyze_numbers(numbers):
     smallest = min(numbers)
     largest = max(numbers)
     total = sum(numbers)
     desc = sorted(numbers, reverse=True)
     return smallest, largest, total, desc

# --- test your function below ---
smallest, largest, total, desc = analyze_numbers([4, 9, 1, 7, 3])
print(smallest)
print(largest)
print(total)
print(desc)