# ask user to input initial stock level, number of months to plan, and sales quantities for each month
initial_stock_level = int(input("Enter initial stock level: "))
num_months = int(input("Enter number of months to plan: "))
sales_quantities = []

for i in range(num_months):
    sales_quantity = int(input(f"Enter planned sales quantity for month {i+1}: "))
    sales_quantities.append(sales_quantity)

# calculate production quantities using zero-stock level strategy
production_quantities = []
previous_stock_level = initial_stock_level
for sales_quantity in sales_quantities:
    if sales_quantity <= previous_stock_level:
        production_quantity = 0
    else:
        production_quantity = sales_quantity - previous_stock_level
    production_quantities.append(production_quantity)
    previous_stock_level = previous_stock_level + production_quantity - sales_quantity

# print results
print(f"Initial stock level: {initial_stock_level}")
print("Sales quantities:", sales_quantities)
print("Production quantities:", production_quantities)
