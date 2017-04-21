from Prac07 import Cars


def main():
    bus = Cars(180)
    bus.drive(30)
    print("fuel =", bus.fuel)
    print("odo =", bus.odometer)
    print(bus)

    print("Car {}, {}".format(bus.fuel, bus.odometer))
    print("{self.name}, {self.fuel}, {self.odometer}".format(self=bus))

    limo = Cars(100)

    bus.add_fuel(20)
    print("fuel = ", bus.fuel)
    limo.drive(115)
    print("odo =", bus.odometer)
    print("{self.name}, {self.fuel}, {self.odometer}".format(self=limo))
main()