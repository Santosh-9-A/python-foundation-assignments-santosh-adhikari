'''Use:
total_rows = 2000
missing_rows = 120
duplicate_rows = 30
“Calculate the total number and percentage of problematic rows.

Classify the dataset using these rules:

At most 2%: Excellent
More than 2% and at most 5%: Acceptable
More than 5%: Needs Cleaning”
Display:

Total rows
Problematic rows
Problem percentage
Final classification
“For this exercise, assume missing rows and duplicate rows do not overlap.”'''

total_rows = 2000
missing_rows = 120
dublicate_rows = 30

#calculate problematic rows
problematic_rows = total_rows+missing_rows

#calculate percentage
problem_percentage = (missing_rows/total_rows)*100

# Classification
if problem_percentage <= 2:
    classification = "Excellent"
elif problem_percentage <= 5:
    classification = "Acceptable"
else:
    classification = "Needs Cleaning"

#Display result
print(f"Total rows: {total_rows}")
print(f"Problematic rows: {problematic_rows}")
print(f"Problem percentage: {problem_percentage:.2f}%")
print(f"Final classification: {classification}")

