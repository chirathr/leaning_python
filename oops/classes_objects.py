class Car:
    # class attributes
    wheels = 4

    def __init__(self, make, model):
        # instance attributes
        self.make = make
        self.model = model

    # instance method
    def print_make(self):
        print(self.make)

    # static method
    @staticmethod
    def make_car_sound():
        print("Vroooooooooooo!..")

    # class method
    @classmethod
    def is_car(cls):
        return cls.wheels == 4



if __name__ == '__main__':
    swift = Car("Maruti", "swift")
    swift.print_make()
    Car.make_car_sound()
    print(Car.is_car())
