def filter_high_sales(sales, threshold):
    return list(filter(lambda x: x > threshold, sales))

print(filter_high_sales([100, 150, 90, 200, 300], 150))

