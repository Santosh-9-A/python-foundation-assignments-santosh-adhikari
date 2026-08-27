'''Writr a function class_average(*scores) that accepts any number of scores and returns their average, rounded to 2 decimal places.

If no scores are passed at all, the function should return 0.

Simple calls and expected output:

class_average(80, 90, 70)
class_average(55, 60, 65, 70, 75)
class_average()

'''

# Write your code here

def class_average(*scores):
    if not scores:
        return 0

    return round(sum(scores) / len(scores), 2)


# --- test your function below ---
print(class_average(80, 90, 70))
print(class_average(55, 60, 65, 70, 75))
print(class_average())