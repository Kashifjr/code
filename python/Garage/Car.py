class Car:
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def __str__(self) -> str:
        return f"{self.year} {self.make} {self.model}"

    def printCar(self):
        print(str(self.year)+" " +self.make+" "+self.model)

    def getCar(self):
        return self

    # FIX: need to return string of self.model
    