from abc import ABC, abstractmethod


# Abstract Base class
class Vehicle(ABC):

    VEHICLE_TYPE_CAR = "car"
    VEHICLE_TYPE_TRUCK = "truck"

    def __init__(self, miles, make, model, year, sold_on):
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on

        if self.vehicle_type() == self.VEHICLE_TYPE_CAR:
            self.base_sale_price = 8000
            self.wheels = 4
        elif self.vehicle_type() == self.VEHICLE_TYPE_TRUCK:
            self.base_sale_price = 10000
            self.wheels = 4

    def sale_price(self):
        """Return the sale price for this vehicle as a float amount."""
        if self.sold_on is not None:
            return 0.0  # Already sold
        return 5000.0 * self.wheels

    def purchase_price(self):
        """Return the price for which we would pay to purchase the vehicle."""
        if self.sold_on is None:
            return 0.0  # Not yet sold
        return self.base_sale_price - (.10 * self.miles)

    @abstractmethod
    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        pass


class Car(Vehicle):
    def vehicle_type(self):
        return Vehicle.VEHICLE_TYPE_CAR


class Truck(Vehicle):
    def vehicle_type(self):
        return Vehicle.VEHICLE_TYPE_TRUCK


if __name__ == '__main__':
    mycar = Car(0, "maruti", 'swift', 2018, None)
    print(mycar.sale_price())

    my_truck = Truck(100, "BharatBenz", "truck", 2017, 10)
    print(my_truck.purchase_price())
