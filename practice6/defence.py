import os
from functools import reduce

folder_path = "sales"

files = os.listdir(folder_path)

products = []

for file in files:
    file_path = os.path.join(folder_path, file)
    
    with open(file_path, "r") as f:
        for line in f:
            name, qty = line.strip().split(",")
            products.append((name, int(qty)))

total_records = len(products)

quantities = list(map(lambda x: x[1], products))

total_quantity = sum(quantities)

average_quantity = total_quantity / total_records if total_records else 0

highest = max(quantities)
lowest = min(quantities)

increased_products = list(map(lambda x: (x[0], x[1] + 2), products))

popular_products = list(filter(lambda x: x[1] > 5, products))

product_of_quantities = reduce(lambda x, y: x * y, quantities)

print("Products with index:")
for i, (name, qty) in enumerate(products, start=1):
    print(i, name, qty)

names = list(map(lambda x: x[0], products))
quantities = list(map(lambda x: x[1], products))
zipped = list(zip(names, quantities))

print("\nZipped result:")
print(zipped)

sorted_products = sorted(products, key=lambda x: x[1])

print("\nSorted products:")
print(sorted_products)

with open("sales_report.txt", "w") as report:
    report.write(f"Total records: {total_records}\n")
    report.write(f"Average quantity sold: {average_quantity:.2f}\n")
    report.write(f"Highest quantity sold: {highest}\n")
    report.write(f"Lowest quantity sold: {lowest}\n\n")
    
    report.write("Popular products:\n")
    for name, qty in popular_products:
        report.write(f"{name} {qty}\n")

print("\nSummary:")
print("Total records:", total_records)
print("Average:", average_quantity)
print("Highest:", highest)
print("Lowest:", lowest)
print("Product of quantities:", product_of_quantities)