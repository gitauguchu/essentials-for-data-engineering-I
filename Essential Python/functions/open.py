def write_sales_to_file(filename, content):
    "Writes content into a file"
    with open(filename, "w") as file:
        file.write(content)

def read_sales_file(filename):
    "Reads file contents"
    with open(filename, "r") as file:
        return file.read()

def append_sales_to_file(filename, content):
    "Appends new content to an exisitng file"
    with open(filename, "a") as file:
        file.write(content)

write_sales_to_file("sales.txt", "Product: Laptop\nSales: 150")
print(read_sales_file("sales.txt"))

append_sales_to_file("sales.txt", "\nProduct: Mouse\nSales: 300")
print(read_sales_file("sales.txt"))

#It is important to close a file once you are done with the operations. This is done using the close() function
#In this case, we use 'with' which automatically closes the file