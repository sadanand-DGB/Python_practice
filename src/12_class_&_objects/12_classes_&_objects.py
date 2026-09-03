class Car:
    showroom = "ABC Motors"  # Class attribute

    def __init__(self, brand):   #constructor method to initialize the brand of the car
        self.brand = brand

    def show_car(self):          # Instance method to display the car's brand
        print(f"Car: {self.brand}")

    @classmethod                               
    def change_showroom(cls, new_showroom):     # Class method to change the showroom name
        cls.showroom = new_showroom

    @staticmethod
    def is_valid_speed(speed):          # Static method to check if the speed is valid (non-negative)
        return speed >= 0

car1 = Car("BMW")      # Create an instance/object of the Car class
car1.show_car()        # Call the instance method to display the car's brand
Car.change_showroom("XYZ Motors")  # Call the class method to change the showroom name
print(Car.showroom)
print(Car.is_valid_speed(100))     # Call the static method to check if the speed is valid