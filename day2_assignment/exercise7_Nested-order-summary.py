'''Given:

orders = {
    "ORD-001": {
        "customer": "Anisha",
        "amount": 2500,
        "status": "Completed"
    },
    "ORD-002": {
        "customer": "Ravi",
        "amount": 1800,
        "status": "Pending"
    },
    "ORD-003": {
        "customer": "Maya",
        "amount": 3200,
        "status": "Completed"
    }
}
Tasks:

Print every order ID and customer.
Print only completed orders.
Calculate the total amount of completed orders.
Count pending orders.
Add a new order to the dictionary.'''


# Nested dictionary
orders = {
    "ORD-001": {
        "customer": "Anisha",
        "amount": 2500,
        "status": "Completed"
    },
    "ORD-002": {
        "customer": "Ravi",
        "amount": 1800,
        "status": "Pending"
    },
    "ORD-003": {
        "customer": "Maya",
        "amount": 3200,
        "status": "Completed"
    }
}

# 1. Print every order ID and customer
print("Order ID and Customer:")
for order_id, details in orders.items():
    print(order_id, "-", details["customer"])

# 2. Print only completed orders
print("\nCompleted Orders:")
for order_id, details in orders.items():
    if details["status"] == "Completed":
        print(order_id, details)

# 3. Calculate the total amount of completed orders
total_completed = sum(
    details["amount"]
    for details in orders.values()
    if details["status"] == "Completed"
)
print("\nTotal Completed Amount:", total_completed)

# 4. Count pending orders
pending_count = sum(
    1 for details in orders.values()
    if details["status"] == "Pending"
)
print("Pending Orders:", pending_count)

# 5. Add a new order
orders["ORD-004"] = {
    "customer": "Nima",
    "amount": 2100,
    "status": "Pending"
}

print("\nUpdated Orders:")
for order_id, details in orders.items():
    print(order_id, details)