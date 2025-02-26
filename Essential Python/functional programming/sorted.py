def sort_sales_data_by_sales(data):
    return sorted(data, key = lambda x: x['Sales'], reverse=True)

sales_data = [
    {'Product' : 'Laptop', 'Sales' : 450},
    {'Product' : 'Mouse', 'Sales' : 200},
    {'Product' : 'Keyboard', 'Sales' : 300},
]

print(sort_sales_data_by_sales(sales_data))