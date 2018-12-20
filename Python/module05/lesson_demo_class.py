class Vehicle:
    """"Main Parent class"""

    # Year depreciation rate
    deprication = 0.9
    # Count of released cars (Created class objects)
    count = 0

    # Class object creation: Vehicle('Toyota', 'Camry', 5000, 1995)
    def __init__(self, produced_by, model, price, year):
        # Init class variables
        self.produced_by = produced_by
        self.model = model
        self.price = price
        self.year = year
        #
        self.mileage=0
        self.count +=1
        self.comment = "Vehicle comment"\


    def drive(self, miles):
        self.mileage += miles

    def decrease_price(self):
        self.price *= self.deprication

    @classmethod
    def set_deprication(cls, deprication):
        cls.deprication = deprication

    @classmethod
    def from_str(cls, vehicle_str):
        return Vehicle(*vehicle_str.split("-"))

    @staticmethod
    def to_km(miles):
        return miles * 1.6

    @property
    def name(self):
        return "{}, {}".format(self.produced_by, self.model)

    @name.setter
    def name(self, name):
        self.produced_by, self.model = name.split(", ")

    @name.deleter
    def name(self):
        pass

    # Magic methods
    def __repr__(self):
        return "Vehicle({}, {}, {} ,{})".format(self.produced_by, self.model, self.price, self.year)

    def __str__(self):
        return "Vehicle {}, produced by {}".format(self.model, self.produced_by)

    def __add__(self, other):
        return self.price + other.price

    def __len__(self):
        return len(self.model)

    def __del__(self):
        pass


class Car(Vehicle):
    def __init__(self, produced_by, model, body_type, price, year):
        super().__init__(produced_by, model, price, year)
        self.body_type = body_type

    @classmethod
    def from_str(cls, vehicle_str):
        return cls(*vehicle_str.split("-"))


class HeavyVehicle(Vehicle):
    deprication = 0.99
    def work(self):
        print("Working hard...")


my_vehicle = Vehicle('Toyota', 'Camry', 5000, 1995)
