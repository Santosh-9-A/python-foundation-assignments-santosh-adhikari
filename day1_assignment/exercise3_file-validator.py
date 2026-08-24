'''“Ask the user to enter a file name.

The program should accept:

.csv
.json
.parquet
The comparison should work even when the user enters uppercase letters.”

Sample values:

sales.csv
CUSTOMERS.JSON
transactions.parquet
report.xlsx
Hint:

file_name = file_name.strip().lower()'''


file_name = input("Enter a file name: ")

file_name = file_name.strip().lower()

if file_name.endswith((".csv", ".json", ".parquet")):
    print("Valid file type.")
else:
    print("Invalid file type.")

