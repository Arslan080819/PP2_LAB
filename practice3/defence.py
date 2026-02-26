class Product:
    total_products=0
    def __init__(self, name, price):
        self.name=name
        Product.total_products +=1
        self.price=price
    def info(self):
        return f"Product: {self.name}, Price: {self.price}"
    
class DigitalProduct(Product):
    def __init__(self,name, price, file_size):
        super().__init__(name,price)
        self.file_size=file_size
    def get_info(self):
        return f"{self.name} ({self.price}) - file size: {self.file_size}"
    
class PhysicalProduct(Product):
    def __init__(self,name,price, weight):
        super().__init__(name,price)
        self.weight=weight
    def get_info(self):
        return f"{self.name} ({self.price}) - weight: {self.weight}"
    
p1=DigitalProduct("Python Course: ", 50, 1500)
p2=PhysicalProduct("Laptop: ", 1200, 2.5)
p3=DigitalProduct("C++ Course :", 60, 2000)

print(p1.get_info)
print(p2.get_info)
print(p3.get_info)
print("Total Products: ", Product.total_products)
