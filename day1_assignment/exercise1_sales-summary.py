''' “Create variables for a product name, unit price, quantity sold, and discount percentage.

Calculate the gross sales, discount amount, and final sales amount.

Display the output using an f-string.”

product_name = "Wireless Mouse"
unit_price = 1500
quantity_sold = 12
discount_percentage = 0.10
Expected format:

Product: Wireless Mouse
Gross sales: NPR 18000.00
Discount: NPR 1800.00
Final sales: NPR 16200.00 '''


product_name = "Wireless Mouse"
unit_price = 1500
quantity_sold = 12
discount_percentage = 0.10

# Calculations
gross_sales = unit_price * quantity_sold
discount_amount = gross_sales * discount_percentage
final_sales = gross_sales - discount_amount

# Output
print(f"Product: {product_name}")
print(f"Gross sales: NPR {gross_sales:.2f}")
print(f"Discount: NPR {discount_amount:.2f}")
print(f"Final sales: NPR {final_sales:.2f}")

