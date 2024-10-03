#How to Define a Class in Python? What Is Self? Give An Example Of A Python Class

class Car:
    def __init__(self, brand, model):
        self.brand = brand  
        self.model = model  

    def display_info(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}")

car1 = Car("Toyota", "Corolla")

car1.display_info()