from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, account_year):
        self.name = name
        self.account_year = account_year

    def account_age(self):
        current_year = 2025
        return current_year - self.account_year

    @abstractmethod
    def get_role(self):
        pass

class Admin(User):
    def get_role(self):
        return "Admin"

    def __str__(self):
        return f"Admin User: {self.name}, Account Age: {self.account_age()} years"

class Guest(User):
    def get_role(self):
        return "Guest"

    def __str__(self):
        return f"Guest User: {self.name}, Account Age: {self.account_age()} years"

admin_user = Admin("Rahul", 2020)
guest_user = Guest("Neha", 2023)

print("Admin Role:", admin_user.get_role())
print("Admin Account Age:", admin_user.account_age())
print(admin_user)

print("\nGuest Role:", guest_user.get_role())
print("Guest Account Age:", guest_user.account_age())
print(guest_user)
