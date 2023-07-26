#        Sales Graph QAP4
#    Written by: Justin Whalen


import matplotlib.pyplot as plt

monthly_sales = []
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Get sales data for each month
for month in months:
    while True:
        try:
            sales_value = float(input(f"Enter total sales for {month}: "))
            monthly_sales.append(sales_value)
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Create the graph
plt.figure(figsize=(10, 6))
plt.plot(months, monthly_sales, marker='o', linestyle='-', color='pink', label='Total Sales ($)')
plt.xlabel('Months')
plt.ylabel('Total Sales ($)')
plt.title('Total Sales by Month')
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.show()