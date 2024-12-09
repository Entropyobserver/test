class Car:
    def __init__(self, make, model, color):
        # Instance variables
        self.make = make
        self.model = model
        self.color = color
    
    def describe(self):
        pass
        # A method
        return f"{self.color} {self.make} {self.model}"


car1 = Car("Toyota", "Camry", "Red")
car2 = Car("Honda", "Civic", "Blue")

print(car1.describe())  # Output: Red Toyota Camry
print(car2.describe())  # Output: Blue Honda Civic
