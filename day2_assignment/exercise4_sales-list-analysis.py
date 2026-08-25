'''Given:

monthly_sales = [85000, 120000, 95000, 140000, 75000, 160000]
Create:

A sorted list from highest to lowest.
A list containing only values above 100000.
A list where each amount has 13% tax added.
The total sales amount.
The average sales amount.

Use comprehensions where appropriate.'''

monthly_sales = [85000, 120000, 95000, 140000, 75000, 160000]

sorted_sales = sorted(monthly_sales, reverse=True)
print(f"Sorted: {sorted_sales}")

for sales in monthly_sales:
    if sales >=100000:
        print(f"Greater or above: {sales}")

for tax in monthly_sales:
    with_tax = (tax*13)/100
    print(f"Tax: {with_tax}")

total_sales = sum(monthly_sales)
print(f"Total: {total_sales}")

average_sales = total_sales/len(monthly_sales)
print(f"Average: {average_sales}")