# import datetime
# # Foydalanuvchidan tug‘ilgan yilini olish
# birth_year = int(input("Tug‘ilgan yilingizni kiriting: "))
# # Hozirgi yilni olish
# current_year = datetime.date.today().year
# # Yoshni hisoblash
# age = current_year - birth_year
# print(f"Siz {age} yoshdasiz.")


# import datetime
# date_input = input("Sanani kiriting (YYYY-MM-DD): ")
# date_obj = datetime.datetime.strptime(date_input, "%Y-%m-%d")
# week_day = date_obj.strftime("%A") # Hafta kunini olish
# print(f"{date_input} - {week_day} kuni bo‘lgan.")
# Bazaviy "Vehicle" klassi
class Vehicle:
    def __init__(self, make, model, year, price):
        self.make = make  # Ishlab chiqaruvchi
        self.model = model  # Modeli
        self.year = year  # Yili
        self.price = price  # Narxi

    def get_info(self):
        # Avtomobil haqida umumiy ma'lumot qaytaradi
        return f"{self.year} {self.make} {self.model}, Price: ${self.price}"

# "Car" klassi, "Vehicle" dan meros oladi
class Car(Vehicle):
    def __init__(self, make, model, year, price, fuel_type):
        super().__init__(make, model, year, price)  # Bazaviy klassdan atributlarni meros olish
        self.fuel_type = fuel_type  # Yoqilg'i turi (masalan, benzin, dizel, elektr)

    def get_info(self):
        # Mashina haqida kengroq ma'lumot qaytaradi
        base_info = super().get_info()  # Bazaviy get_info funksiyasidan foydalanadi
        return f"{base_info}, Fuel Type: {self.fuel_type}"

# "Motorcycle" klassi, "Vehicle" dan meros oladi
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, price, max_speed):
        super().__init__(make, model, year, price)  # Bazaviy klassdan atributlarni meros olish
        self.max_speed = max_speed  # Maksimal tezlik

    def get_info(self):
        # Mototsikl haqida kengroq ma'lumot qaytaradi
        base_info = super().get_info()  # Bazaviy get_info funksiyasidan foydalanadi
        return f"{base_info}, Max Speed: {self.max_speed} km/h"
# Ob'ektlarni yaratish

car = Car("Toyota", "Supra", 2002, 40000, "Petrol")
car2 = Car("Dodge", "Challenger", 2022, 35000, "Petrol")
motorcycle = Motorcycle("Yamaha", "YZF-R3", 2022, 6000, 180)
motorcycle2 = Motorcycle("BMW", "SR-1000", 2019, 15000, 300)

# Ma'lumotlarni chiqarish
print(car.get_info())  # "2023 Toyota Camry, Price: $30000, Fuel Type: Petrol"
print(motorcycle.get_info())  # "2022 Yamaha YZF-R3, Price: $6000, Max Speed: 180 km/h"
print(car2.get_info())
print(motorcycle2.get_info())
