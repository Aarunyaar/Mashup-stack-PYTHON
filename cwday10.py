from abc import ABC, abstractmethod
from datetime import datetime

class User(ABC):
    def __init__(self, name, joining_year):
        self.name = name
        self.joining_year = joining_year

    def years_on_platform(self):
        current_year = 2025
        return current_year - self.joining_year

    @abstractmethod
    def role(self):
        pass

    def __str__(self):
        return f"{self.name} - {self.role()} - Using platform for {self.years_on_platform()} years"

class Customer(User):
    def role(self):
        return "Customer"

class Vendor(User):
    def role(self):
        return "Vendor"

if __name__ == "__main__":
    customer = Customer("Aarav", 2020)
    vendor = Vendor("Meera", 2018)

    print(customer)
    print(vendor)
