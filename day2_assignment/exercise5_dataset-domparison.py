'''Given:

dataset_a = {
    "customer",
    "sales",
    "product",
    "employee"
}

dataset_b = {
    "sales",
    "product",
    "supplier",
    "inventory"
}
Find:

All unique dataset names
Datasets found in both groups
Datasets only in dataset_a
Datasets only in dataset_b
Display each result clearly.'''

dataset_a = {
    "customer",
    "sales",
    "product",
    "employee"
}

dataset_b = {
    "sales",
    "product",
    "supplier",
    "inventory"
}


unique_dataset = dataset_a|dataset_b
print(f"Unique Dataset: {unique_dataset}")

both_dataset = dataset_a & dataset_b
print(f"Both Dataset: {both_dataset}")

only_dataset_a = dataset_a - dataset_b
print(f"Only Dataset_a: {only_dataset_a}")

only_dataset_b = dataset_b - dataset_a
print(f"Only Dataset_b: {only_dataset_b}")