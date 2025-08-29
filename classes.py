class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"Device: {self.brand} {self.model}"


class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
       
        super().__init__(brand, model)
        
        self.os = os
        self.storage = storage
        self.__battery = 100 

    def install_app(self, app_name):
        return f"Installing {app_name} on {self.brand} {self.model}..."

    def use_battery(self, amount):
        if self.__battery - amount < 0:
            self.__battery = 0
        else:
            self.__battery -= amount
        return f"Battery level: {self.__battery}%"


# Example usage
phone1 = Smartphone("Apple", "iPhone 15", "iOS", "256GB")
phone2 = Smartphone("Samsung", "Galaxy S23", "Android", "512GB")

print(phone1.device_info())
print(phone1.install_app("WhatsApp"))
print(phone1.use_battery(30))


print("\n--- Device 2 ---")
print(phone2.device_info())
print(phone2.install_app("Instagram"))
