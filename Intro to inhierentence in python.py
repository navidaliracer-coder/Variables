class vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(vehicle):
    pass

School_bus = Bus("School bus", 180, 12)
print("Vehicle Name:", School_bus.name, "Speed:" School_bus.speed, "Mileage:",  School_bus.mileage)

        