from Prac07.cars import Cars


def main():
    bus = Cars("Bus", 180)
    bus.drive(30)
    print("fuel =", bus.fuel)
    print("odo =", bus.odometer)
    print(bus)

    print("Car {}, {}".format(bus.fuel, bus.odometer))
    print("{self.name}, {self.fuel}, {self.odometer}".format(self=bus))

    limo = Cars("Limo", 100)
    limo.add_fuel(20)
    print("fuel = ", limo.fuel)
    limo.drive(115)
    print("{self.name}, {self.fuel}, {self.odometer}".format(self=limo))


main()