class SmartPhone():
    def __init__(self):
        self._company = "Apple"
        self._firmware = 10.0

    def get_os_version(self):
        return self._firmware

    def update_firmware(self):
        print("Reaching out to the server for the next version")
        self._firmware += 1

iphone = SmartPhone()
print(iphone._company) #op: Apple
print(iphone._firmware) #op: 10.0

print(iphone.update_firmware()) #op: None 
print(iphone._firmware) #op: 11.0

